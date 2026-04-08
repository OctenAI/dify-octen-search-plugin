# Octen Search Plugin for Dify

Real-time web search for AI agents powered by [Octen](https://octen.ai). Delivers LLM-native search results with industry-leading latency (62ms P50).

## Features

- **Ultra-low latency**: 62ms P50, at least 4x faster than alternatives
- **Real-time results**: New content indexed within 5 minutes of publication
- **Domain filtering**: Include or exclude specific domains
- **Time-based filtering**: Filter results by publication date
- **Safe search**: Built-in content safety filtering
- **LLM-optimized**: Results formatted for AI agent consumption

## Setup

1. Get your API key from the [Octen Platform](https://octen.ai/platform)
2. Install this plugin in your Dify instance
3. Enter your Octen API key in the plugin credentials

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search query (max 500 chars) |
| count | number | No | Number of results (1-100, default 5) |
| include_domains | string | No | Comma-separated domains to include |
| exclude_domains | string | No | Comma-separated domains to exclude |
| start_time | string | No | ISO 8601 start timestamp |
| end_time | string | No | ISO 8601 end timestamp |
| format | select | No | Content format: markdown or text |
| safesearch | select | No | Safe search: strict or off |

## Links

- [Octen Website](https://octen.ai)
- [Octen API Documentation](https://docs.octen.ai/api-reference/web-search)
- [Octen Platform](https://octen.ai/platform)

## Contact

- GitHub: [octen-ai](https://github.com/octen-ai)
- Website: [octen.ai](https://octen.ai)
