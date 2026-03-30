from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def generate_trends():
    topics = ["AI Tools", "E-commerce", "Crypto", "Fitness Apps", "Online Courses"]
    data = []
    for t in topics:
        growth = random.randint(40,100)
        competition = random.randint(20,100)
        score = round((growth*0.7)-(competition*0.3),2)
        data.append({
            "topic": t,
            "growth": growth,
            "competition": competition,
            "score": score
        })
    return data

@app.route("/api/trends")
def trends():
    return jsonify(generate_trends())

if __name__ == "__main__":
    app.run(debug=True)
