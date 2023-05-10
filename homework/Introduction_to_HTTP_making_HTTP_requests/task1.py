import requests

# Download and save the robots.txt file for Wikipedia
wikipedia_url = 'https://en.wikipedia.org/robots.txt'
wikipedia_response = requests.get(wikipedia_url)
with open('wikipedia_robots.txt', 'wb') as f:
    f.write(wikipedia_response.content)

# Download and save the robots.txt file for Twitter
twitter_url = 'https://twitter.com/robots.txt'
twitter_response = requests.get(twitter_url)
with open('twitter_robots.txt', 'wb') as f:
    f.write(twitter_response.content)