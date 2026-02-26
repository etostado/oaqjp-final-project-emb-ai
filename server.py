"""
Flask web server for the Emotion Detection application.

Serves the UI (index.html) and exposes an endpoint /emotionDetector that
returns formatted emotion analysis results.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

APP_HOST = "0.0.0.0"
APP_PORT = 5000

app = Flask(__name__)


@app.route("/")
def render_index():
    """Render the main UI page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    Analyze user text and return a formatted response string.

    The provided UI sends a GET request with query param 'textToAnalyze'.
    If blank/invalid input is provided, returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)
