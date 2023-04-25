import requests
import json
from multiprocessing.pool import ThreadPool

url = 'https://api.pushshift.io/reddit/comment/search/CookieClicker'
params = {'sort': 'asc', 'sort_type': 'created_utc', 'size': 1000}

# Define a function that retrieves comments from the API and returns them as a list
def get_comments(start):
    params['after'] = start
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        return data

# Use a thread pool to retrieve comments from the API in parallel
pool = ThreadPool(processes=10)
results = []
start_time = 0
while True:
    data = pool.apply(get_comments, (start_time,))
    if not data:
        break
    results.extend(data)
    start_time = data[-1]['created_utc']
    params['before'] = start_time

# Sort the comments in chronological order and dump them to a JSON file
results.sort(key=lambda x: x['created_utc'])
with open('cookieclicker_comments.json', 'w') as outfile:
    json.dump(results, outfile)