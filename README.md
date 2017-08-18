[![Build Status](https://travis-ci.org/james-cube/firefox-bookmarks-deduplicator.svg?branch=master)](https://travis-ci.org/james-cube/firefox-bookmarks-deduplicator)

# firefox-bookmarks-deduplicator

Tool for cleaning up firefox bookmarks backups. Designed for people who don't want to do that using firefox plugins. My personal use case is merging and versioning backups from many computers, while not using cloud based solutions like Sync.

1. Removes duplicate bookmakrs
2. Merges directories with same name.

## Usage

### How to backup/restore firefox bookmarks? (up to date with Firefox 54)

In top menu `Bookmarks` under `Show All Bookmarks` there is button `Import and Backup` which allows you to perform those operations either using `json` or `html` file. This module uses and generates `json` backups. 

### How to use the tool?

`python firefox_bookmarks_merger --file bookmarks-20XX-XX-XX.json --output cleaned.json`

### All program arguments

```
usage: firefox_bookmarks_deduplicator [-h] --file FILE --output OUTPUT

optional arguments:
  -h, --help       show this help message and exit
  --file FILE      File to process
  --output OUTPUT  Output file
```

### My other tools 

[Firefox Session Merger](https://github.com/james-cube/firefox-session-merger)

[Firefox Bookmarks Merger](https://github.com/james-cube/firefox-bookmarks-merger)
