from flask import Flask, jsonify
from database import engine, Base
from services.trend_service import generate_and_store_trends

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

@app.route("/api/generate")
def generate():
    trends = generate_and_store_trends()

    return jsonify([
        {
            "topic": t.topic,
            "score": t.score
        } for t in trends
    ])

if __name__ == "__main__":
    app.run(debug=True)