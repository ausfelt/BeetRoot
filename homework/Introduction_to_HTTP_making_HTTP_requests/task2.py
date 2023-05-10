import requests
import json

url = "https://api.pushshift.io/reddit/comment/search/?q=universe&before=30d&sort=score&sort_type=asc&size=1000"

all_comments = []

while True:
    response = requests.get(url)
    data = json.loads(response.text)
    comments = data["data"]
    if not comments:
        break
    all_comments.extend(comments)

    # Get the timestamp of the oldest comment
    oldest_comment = comments[-1]
    timestamp = oldest_comment["created_utc"]

    # Set the URL for the next request to get the next batch of comments
    url = f"https://api.pushshift.io/reddit/comment/search/?q=universe&before={timestamp}&sort=score&sort_type=asc&size=1000"

# Save the comments to a JSON file
with open("universe_comments.json", "w") as f:
    json.dump(all_comments, f)