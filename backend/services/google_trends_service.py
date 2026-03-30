import random

def fetch_google_trends():
    topics = [
        "AI business",
        "Online income",
        "SaaS tools",
        "Digital marketing",
        "Crypto trends"
    ]

    trends = []

    for t in topics:
        trends.append({
            "topic": t,
            "growth": random.randint(50, 100)
        })

    return trends