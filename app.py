from flask import Flask, request, jsonify
from extensions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
from models import URL


@app.route("/")
def home():
    return "URL Shortener API is running!"

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    return jsonify({
        "received_url": data["url"]
    })
    
if __name__ == "__main__":
    app.run(debug=True)