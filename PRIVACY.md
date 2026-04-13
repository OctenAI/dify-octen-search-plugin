# Privacy Policy for Octen Search Plugin

This privacy policy describes how the Octen Search Plugin for Dify ("we", "our", or "us") collects, uses, and protects your information when you use our web search service.

_Last updated: 2026-04-13_

## Data Collection

### What We Collect

- **Search Queries**: The text query you submit to perform a web search.
- **Search Parameters**: Optional filter parameters you provide, including `count`, `include_domains`, `exclude_domains`, `include_text`, `exclude_text`, `time_basis`, `start_time`, `end_time`, `highlight_enabled`, `highlight_max_tokens`, `full_content_enabled`, `full_content_max_tokens`, `format`, and `safesearch`.
- **Authentication Data**: Your Octen API key, which is required to authenticate requests to the Octen Search API.

### What We Don't Collect

- The plugin does not collect names, emails, phone numbers, addresses, government IDs, biometric data, or payment information.
- The plugin does not track device identifiers, IP addresses, location data, cookies, or browsing history beyond what is necessary to fulfill the search request.
- The plugin does not store search queries, results, or credentials locally. It acts only as a pass-through client between the Dify runtime and the Octen Search API.

> **Note**: If you voluntarily include personal or sensitive information in a search query, that content will be transmitted to the Octen Search API as part of the query payload. Users are responsible for the content of queries they submit.

## How We Use Your Data

- **Service Provision**: Search queries and parameters are sent to the Octen Search API solely to retrieve search results and return them to your Dify application.
- **Authentication**: Your Octen API key is used only to authenticate requests to the Octen Search API.
- **No Plugin-Side Analytics**: This plugin does not perform any analytics, logging, profiling, or advertising. It does not retain data after a request is served.

## Third-Party Services

### Octen Search API

This plugin integrates with the Octen Search API (`https://api.octen.ai/search`). When you invoke the plugin:

- Your search query, filter parameters, and API key are transmitted over HTTPS to Octen's servers for processing.
- Octen's handling of transmitted data is governed by Octen's own terms and privacy practices. Please review them at [https://octen.ai](https://octen.ai) before use.
- Octen may retain request metadata (e.g., for rate limiting, billing, and abuse prevention) according to its own policy.

### Dify Platform

This plugin runs within the Dify platform. Dify's privacy policy applies to the Dify runtime environment. Please refer to Dify's privacy policy for details: [https://dify.ai/privacy](https://dify.ai/privacy).

## Data Retention

- **Search Queries and Results**: Not retained by this plugin. They exist in memory only for the duration of the request.
- **Authentication Data**: Your Octen API key is stored by the Dify platform as a plugin credential (handled as a `secret-input` field) and is transmitted only to the Octen Search API when the tool is invoked. It is not logged or stored by the plugin itself.
- **Octen-Side Retention**: Any retention by Octen is governed by Octen's policies.

## Data Security

- All traffic between the plugin and the Octen Search API is encrypted in transit via HTTPS.
- Your API key is stored as a secret credential by the Dify platform and is never written to logs or output messages by the plugin.
- While we follow industry-standard practices, no internet transmission is 100% secure. You are responsible for safeguarding your API key.

## Children's Privacy

This plugin is not intended for use by children under 13 and does not knowingly collect personal information from children.

## International Data Transfers

Because the Octen Search API may process requests in jurisdictions different from your own, your query data may cross international borders. By using this plugin, you acknowledge and consent to such transfers.

## Changes to This Privacy Policy

We may update this privacy policy from time to time. Updates will be reflected in this file and indicated by a revised "Last updated" date.

## Contact

For questions about this policy or the plugin:

- GitHub: [https://github.com/OctenAI](https://github.com/OctenAI)
- Website: [https://octen.ai](https://octen.ai)

For questions about Octen Search API data handling, contact Octen directly via [https://octen.ai](https://octen.ai).
