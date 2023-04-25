import requests
import json
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def download_comments(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']


def main():
    subreddit = 'sweden'
    url_template = 'https://api.pushshift.io/reddit/comment/search/?subreddit={}&size=100&sort=desc&before='
    before = ''
    all_comments = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        while True:
            url = url_template.format(subreddit) + before
            results = pool.submit(download_comments, url).result()
            if not results:
                break
            all_comments.extend(results)
            before = str(results[-1]['created_utc'])
    with open('sweden_comments.json', 'w') as f:
        json.dump(all_comments, f, indent=2)


if __name__ == '__main__':
    main()

#Still cant get the comments to download, but I think I'm on the right track.