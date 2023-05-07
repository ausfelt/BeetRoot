import asyncio
import aiohttp
import json

async def download_comments(subreddit):
    url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}&size=100"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data['data']

async def main():
    subreddit = "science"
    comments = []
    after = None
    while len(comments) < 50:
        data = await download_comments(subreddit)
        if not data:
            break
        comments += data
        after = comments[-1]['created_utc']
        print(f"Downloaded {len(comments)} comments so far...")
    comments.sort(key=lambda x: x['created_utc'])
    with open(f"{subreddit}_comments.json", "w") as f:
        json.dump(comments[:50], f)
    print(f"Downloaded {len(comments[:50])} comments in total")

asyncio.run(main())