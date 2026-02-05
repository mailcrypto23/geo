import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def health():
    return {"status": "ok"}

@app.route("/markets")
def markets():
    tag = request.args.get("tag", "geopolitics")
    limit = request.args.get("limit", "5")

    url = (
        "https://gamma-api.polymarket.com/markets"
        f"?tag={tag}&closed=false&limit={limit}"
    )

    r = requests.get(url, headers={"accept": "application/json"}, timeout=15)
    return jsonify(r.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)