from database import SessionLocal
from models import Trend
from services.ai_service import compute_score
from services.reddit_service import fetch_reddit_trends
from services.google_trends_service import fetch_google_trends
import random

def generate_and_store_trends():
    db = SessionLocal()

    reddit_trends = fetch_reddit_trends()
    google_trends = fetch_google_trends()

    all_trends = reddit_trends + google_trends

    results = []

    for t in all_trends:
        growth = t["growth"]
        competition = random.randint(20, 80)

        score = compute_score(growth, competition)

        trend = Trend(
            topic=t["topic"],
            growth=growth,
            competition=competition,
            score=score
        )

        db.add(trend)
        results.append(trend)

    db.commit()
    db.close()

    return results