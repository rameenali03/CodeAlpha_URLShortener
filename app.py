from datetime import datetime

import secrets
import string

from flask import Flask, request, jsonify, redirect
from extensions import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
from models import URL

@app.route("/")
def home():
    return "URL Shortener API is running!"

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        short_code = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        existing_url = db.session.scalar(
            db.select(URL).where(URL.short_code == short_code)
        )

        if existing_url is None:
            return short_code
       
@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json(silent=True)

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    original_url = data["url"].strip()

    if not original_url:
        return jsonify({"error": "URL cannot be empty"}), 400

    if not original_url.startswith(("http://", "https://")):
        return jsonify({
            "error": "URL must start with http:// or https://"
        }), 400

    short_code = generate_short_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code,
        created_at=datetime.utcnow()
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://127.0.0.1:5000/{short_code}"
    }), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_to_original(short_code):
    url = db.session.scalar(
        db.select(URL).where(URL.short_code == short_code)
    )

    if url is None:
        return jsonify({"error": "Short URL not found"}), 404

    url.click_count += 1
    db.session.commit()

    return redirect(url.original_url)


if __name__ == "__main__":
    app.run(debug=True)

