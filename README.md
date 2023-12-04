# aoc-leaderboard
Advent of Code leaderboad slack integration.

Posts leaderboard summary to the given slack channel. 

## PreRequisites
1. Python > 3.7 installed.
2. A slack Bot User with permissions to post to the desired slack channel.
3. An Advent of Code account with a private leaderboard set up.

## Setup 

1. Create venv for the project
```
python -m venv venv
source ./venv/bin/activate
```
2. Populate .env file
`cp .env.example .env`
3. Source .env file
`set -a; source .env; set +a`

## Usage

`./get_leaderboard_json.sh`

This will print the output to the console as well as send the payload to slack.

By default, the code will return only the top 10 ranks. This can be adjusted by
changing the LIMIT constant in parse_leaderboard.py.