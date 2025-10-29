# Multi-platform live streaming (draft)

This document describes the initial adapter-based approach to support multiple live streaming platforms.

Supported (stubbed) platforms in this branch:
- TikTok
- BIGO
- YouTube Live
- Uplive
- LiveMe

What was added:
- A small StreamingAdapter interface (src/streaming/adapter.ts)
- Per-platform adapter stubs (src/streaming/adapters/*)
- A simple PlatformSelector React component (frontend/components/PlatformSelector.tsx)
- Exports index for streaming (src/streaming/index.ts)

Next steps / TODOs:
- Implement platform-specific authentication flows (OAuth2 or API keys) for each platform.
- Integrate official SDKs or use RTMP endpoints where applicable.
- Add server-side components to securely store tokens and generate push URLs.
- Add tests and CI checks for adapter behavior and UI.

Notes:
- No credentials or secrets have been added to the repository. All adapters are intentionally stubbed and log actions to the console.
- This branch is intended as a scaffolding step to remove the Spotify-only assumption and provide a place to implement full integrations.
