# Octen Search Plugin for Dify

Real-time web search for AI agents powered by [Octen](https://octen.ai). Delivers LLM-native search results with industry-leading latency (62ms P50).

## Features

- **Ultra-low latency**: 62ms P50, at least 4x faster than alternatives
- **Real-time results**: New content indexed within 5 minutes of publication
- **Domain filtering**: Include or exclude specific domains
- **Text filtering**: Require or exclude specific text in results
- **Time-based filtering**: Filter results by publication or crawl date
- **Full content extraction**: Retrieve full page content with configurable token limits
- **Highlight snippets**: Query-relevant highlights with configurable length
- **Safe search**: Built-in content safety filtering
- **LLM-optimized**: Results formatted for AI agent consumption

## Setup

1. Get your API key from the [Octen Platform](https://octen.ai/platform)
2. Install this plugin in your Dify instance
3. Enter your Octen API key in the plugin credentials

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | Yes | — | Search query (max 500 chars) |
| count | number | No | 5 | Number of results to return (1-100) |
| include_domains | string | No | — | Comma-separated domains to include (max 1000 items) |
| exclude_domains | string | No | — | Comma-separated domains to exclude (max 150 items) |
| include_text | string | No | — | Comma-separated strings that must appear in results (max 5 items) |
| exclude_text | string | No | — | Comma-separated strings that must not appear in results (max 5 items) |
| time_basis | select | No | auto | Time field for filtering: auto, published, or crawled |
| start_time | string | No | — | Filter results after this time (ISO 8601) |
| end_time | string | No | — | Filter results before this time (ISO 8601) |
| highlight_enabled | boolean | No | true | Enable query-relevant highlight snippets |
| highlight_max_tokens | number | No | 512 | Max tokens per highlight (100-20000) |
| full_content_enabled | boolean | No | false | Enable full page content extraction |
| full_content_max_tokens | number | No | 2048 | Max tokens per full content (100-100000) |
| format | select | No | text | Highlight format: markdown or text |
| safesearch | select | No | strict | Content filtering: strict or off |

## Links

- [Octen Website](https://octen.ai)
- [Octen API Documentation](https://docs.octen.ai/api-reference/web-search)
- [Octen Platform](https://octen.ai/platform)
- [Source Code](https://github.com/OctenAI/dify-octen-search-plugin)

## Contact

- GitHub: [OctenAI](https://github.com/OctenAI)
- Website: [octen.ai](https://octen.ai)
