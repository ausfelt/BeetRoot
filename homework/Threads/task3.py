import requests
import json
import os
import requests
import json
import os
from multiprocessing import Pool

SUBREDDIT = 'sweden'
URL = f'https://api.pushshift.io/reddit/comment/search/?subreddit={SUBREDDIT}&sort=desc&size=1000'
OUTPUT_FILE = f'{SUBREDDIT}_comments.json'


def fetch_comments(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []


def download_comments(output_file):
    comments = []
    pool = Pool(processes=os.cpu_count())

    while True:
        response = fetch_comments(URL)
        if not response:
            break

        pool_results = pool.map(fetch_comments, [f'{URL}&before={comment["created_utc"]}' for comment in response])
        for result in pool_results:
            comments.extend(result)

    with open(output_file, 'w') as f:
        json.dump(comments, f)

    print(f'{len(comments)} comments downloaded and saved to {OUTPUT_FILE}')


if __name__ == '__main__':
    download_comments(OUTPUT_FILE)
