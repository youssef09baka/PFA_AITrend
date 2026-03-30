import requests

def fetch_reddit_trends():
    url = "https://www.reddit.com/r/technology/top.json?limit=5"
    
    headers = {"User-Agent": "trend-app"}

    response = requests.get(url, headers=headers)
    data = response.json()

    trends = []

    for post in data["data"]["children"]:
        title = post["data"]["title"]
        score = post["data"]["score"]

        trends.append({
            "topic": title,
            "growth": score
        })

    return trends