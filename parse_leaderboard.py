import json
import sys


def parse_json(filename):
    # read file
    with open(filename, 'r') as json_file:
        data = json_file.read()

    # parse file and get top 10
    json_data = json.loads(data)
    scores = [(user["local_score"], user['name']) for user in json_data["members"].values()]
    scores.sort(reverse=True)
    top_scores = scores[:10]

    output = "Rank|Score|Stars-4-5-6-7-8-9-0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-5-|Name---------------------|"
    print(output)
    for rank, score_tuple in enumerate(top_scores):
        member_record = [member for member in json_data["members"].values() if member["name"] == score_tuple[1]][0]
        output += "\n" + format_output(member_record, rank + 1)

    with open('parsed_data.json', 'w') as parsed_file:
        output = "```" + output + "```"
        parsed_file.write(json.dumps({"text": output}))


def format_output(member_record, rank):
    padded_score = f"{member_record['local_score']}     "[:5]
    stars = []
    for day in range(1, 26):
        if member_record['completion_day_level'].get(str(day), {}).get("1"):
            stars.insert((day-1)*2, "*")
        else:
            stars.insert((day-1)*2, ' ')
        if member_record['completion_day_level'].get(str(day), {}).get("2"):
            stars.insert(day*2, "*")
        else:
            stars.insert(day*2, ' ')

    output_string = "{0}   |{1}|{2}|{3}".format(
        rank,
        padded_score,
        "".join(stars),
        member_record['name']
    )
    print(output_string)
    return output_string


if __name__ == "__main__":
    parse_json(sys.argv[1])
