# Normalize Timezone Name (CSV)

## Purpose

This script was developed for normalizing raw logs' timezone notation/name before the logs are fed into Splunk.
This was required because some of the timezone naming convention were non-standard, for example:

- `HKT` was named as `Hong Kong Summer Time`
- `JPT` was named as `Japan Daylight Time`

## Input

Expected input file name: `log.csv`

Tested with CSV, should work with any text based files.

## Output

Output file: `processed-log.csv`

## How It Works

The script reads input file line by line, and use the following Regular Expression to identify timestamps:

`[0-9]{2}-\w{3}-[0-9]{4}\s[0-9]{2}:[0-9]{2}`

The reason for using `[0-9]` is because the character group `/d` sometimes doesn't recognize numbers properly.

When a timestamp is found, it'll replace the timestamp notation in the following way:

- `Hong Kong Summer Time` -> `HKT`
- `British Summer Time` -> `BST`
- `Japan Daylight Time` -> `JST`
- `Greenwich Mean Time` -> `GDT`
