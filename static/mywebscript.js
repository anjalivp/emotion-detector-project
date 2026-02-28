// Function triggered when the "Run Emotion Detection" button is clicked
function runEmotionDetection() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Build query string for GET request
    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("result").innerHTML = data;
        })
        .catch(error => {
            document.getElementById("result").innerHTML = "Error occurred while processing.";
            console.error("Error:", error);
        });
}
