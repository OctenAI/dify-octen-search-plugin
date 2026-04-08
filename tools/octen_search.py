from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

OCTEN_API_URL = "https://api.octen.ai/search"


class OctenSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        api_key = self.runtime.credentials.get("octen_api_key")
        if not api_key:
            yield self.create_text_message(
                "Octen API key is missing. Please set it in the credentials."
            )
            return

        query = tool_parameters.get("query", "")
        if not query:
            yield self.create_text_message("Please provide a search query.")
            return

        headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }

        payload: dict[str, Any] = {"query": query}

        # count
        if count := tool_parameters.get("count"):
            payload["count"] = int(count)

        # domain filters
        if include_domains := tool_parameters.get("include_domains"):
            payload["include_domains"] = [
                d.strip() for d in include_domains.split(",") if d.strip()
            ]

        if exclude_domains := tool_parameters.get("exclude_domains"):
            payload["exclude_domains"] = [
                d.strip() for d in exclude_domains.split(",") if d.strip()
            ]

        # text filters
        if include_text := tool_parameters.get("include_text"):
            payload["include_text"] = [
                t.strip() for t in include_text.split(",") if t.strip()
            ]

        if exclude_text := tool_parameters.get("exclude_text"):
            payload["exclude_text"] = [
                t.strip() for t in exclude_text.split(",") if t.strip()
            ]

        # time filters
        if time_basis := tool_parameters.get("time_basis"):
            payload["time_basis"] = time_basis

        if start_time := tool_parameters.get("start_time"):
            payload["start_time"] = start_time

        if end_time := tool_parameters.get("end_time"):
            payload["end_time"] = end_time

        # highlight
        highlight_enabled = tool_parameters.get("highlight_enabled", True)
        highlight_max_tokens = tool_parameters.get("highlight_max_tokens", 512)
        payload["highlight"] = {
            "enable": highlight_enabled,
            "max_tokens": int(highlight_max_tokens),
        }

        # full content
        full_content_enabled = tool_parameters.get("full_content_enabled", False)
        if full_content_enabled:
            full_content_max_tokens = tool_parameters.get("full_content_max_tokens", 2048)
            payload["full_content"] = {
                "enable": True,
                "max_tokens": int(full_content_max_tokens),
            }

        # format & safesearch
        if fmt := tool_parameters.get("format"):
            payload["format"] = fmt

        if safesearch := tool_parameters.get("safesearch"):
            payload["safesearch"] = safesearch

        try:
            response = requests.post(
                url=OCTEN_API_URL, json=payload, headers=headers, timeout=30
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            yield self.create_text_message(
                f"Octen API error: {e.response.status_code} - {e.response.text}"
            )
            return
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(f"Request failed: {str(e)}")
            return

        data = response.json()

        if data.get("code") != 0:
            yield self.create_text_message(
                f"Octen search error: {data.get('msg', 'Unknown error')}"
            )
            return

        results = data.get("data", {}).get("results", [])
        if not results:
            yield self.create_text_message(f"No results found for '{query}'.")
            return

        yield self.create_json_message(data.get("data", {}))

        text_lines = []
        for idx, result in enumerate(results, 1):
            title = result.get("title", "No Title")
            url = result.get("url", "")
            highlight = result.get("highlight", "")
            full_content = result.get("full_content", "")
            authors = result.get("authors", "")
            published = result.get("time_published", "")

            text_lines.append(f"## {idx}. [{title}]({url})")
            if authors:
                text_lines.append(f"**Source:** {authors}")
            if published:
                text_lines.append(f"**Published:** {published}")
            if highlight:
                text_lines.append(f"{highlight}")
            if full_content:
                text_lines.append(f"\n**Full Content:**\n{full_content}")
            text_lines.append("")

        yield self.create_text_message("\n".join(text_lines))
