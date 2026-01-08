# YouTube RSS manager

## Archived

This repo has been archived, as the main [ytrssil app](https://github.com/TheEdgeOfRage/ytrssil) now has a frontend with many more feature that are not supported by the CLI.

## About

This is a simple CLI to manage YouTube subscriptions through RSS feeds
and watch new videos using `mpv`.

## Configuration

It looks for a configuration in `$XDG_CONFIG_HOME/ytrssil/config.json`
(~/.config/ by default).

Example:

```json
{
    "token": "token",
    "api_url": "https://example.com",
    "max_resolution": "1080"
}
```
