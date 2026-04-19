"""Flask server for the Emotion Detector web application."""
import os
import sys
from flask import Flask, render_template, request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from EmotionDetection.emotion_detection import emotion_detector  # noqa: E402

_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask("Emotion Detector",
            template_folder=os.path.join(_dir, "templates"),
            static_folder=os.path.join(_dir, "static"))


@app.route("/emotionDetector")
def sent_detector():
    """Analyse text emotion and return a formatted response string."""
    text_to_analyse = request.args.get("textToAnalyse")
    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Serve the main application page."""
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
