"""
Flask server — Feishu Bitable automation endpoints.
Showcase version: routing only.
"""

from flask import Flask, request, jsonify
from pipelines.storyboard import StoryboardPipeline

app = Flask(__name__)
pipeline = StoryboardPipeline()


@app.route("/api/feishu/storyboard", methods=["POST"])
def handle_storyboard():
    payload = request.get_json()
    # [Async dispatch + dynamic table_id routing not shown]
    return jsonify({"code": 0})


@app.route("/api/feishu/analyze", methods=["POST"])
def handle_analyze():
    # [Selling-points analysis route not shown]
    return jsonify({"code": 0})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8200)
