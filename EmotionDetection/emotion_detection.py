import requests
import json

def emotion_detector(text_to_analyse):
    """
    Calls the Watson NLP Emotion Prediction API and returns
    the dominant emotion along with all emotion scores.
    Returns None values for invalid input.
    """

    url = "https://sn-watson-emotion-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-bert-workflow_lang_multi_stock"}

    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        # Convert raw text response into dictionary
        formatted_response = json.loads(response.text)

        # Extract emotion scores
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "emotion": dominant_emotion,
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"]
        }

    except Exception:
        # If invalid text or API error → return None values
        return {
            "emotion": None,
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
