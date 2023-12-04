#!/usr/bin/env bash
set -Eeuo pipefail

# download leaderboard JSON from advent of code API
curl --location --request GET $AOC_LEADERBOARD_URL \
--header "Cookie: session=$AOC_SESSION_COOKIE" \
> leaderboard.json

# format leaderboard JSON for slack message
python parse_leaderboard.py leaderboard.json

# post formatted leaderboard results to slack channel
curl -X POST -H  'Content-type: application/json' -d @parsed_data.json $SLACK_CHANNEL_WEBHOOK