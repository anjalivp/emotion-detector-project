from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the main HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze_emotion():
    """Handle emotion detection requests from the frontend."""
    
    # Read text input from GET request
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle blank input
    if not text_to_analyze:
        return "Invalid input! Try again."

    # Call the emotion detector
    result = emotion_detector(text_to_analyze)

    # Handle invalid emotion output (error from Watson API)
    if result["emotion"] is None:
        return "Invalid input! Try again."

    # Extract values
    emotion = result["emotion"]
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]

    # Build response text
    return (
        f"For the given statement, the dominant emotion is {emotion}."
        f"<br>anger: {anger}"
        f"<br>disgust: {disgust}"
        f"<br>fear: {fear}"
        f"<br>joy: {joy}"
        f"<br>sadness: {sadness}"
    )


if __name__ == "__main__":
    # Run on the required port for submission
    app.run(host="0.0.0.0", port=5000)
