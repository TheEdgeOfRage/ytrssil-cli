# YouTube RSS manager

This is a simple CLI to manage YouTube subscriptions through RSS feeds
and watch new videos using `mpv`. It keeps track of watched videos in a local
sqlite database.

**This tool is still in early development and breaking changes across minor
versions are expected.**

## Configuration

It looks for a list of RSS URLs in `$XDG_CONFIG_HOME/ytrssil/feeds`
(~/.config/ by default), with one URL per line. Only YouTube channel feeds
are supported at this moment.
