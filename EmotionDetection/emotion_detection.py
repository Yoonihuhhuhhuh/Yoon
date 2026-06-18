import requests
import json

def emotion_detector(text_to_analyse):
    
    if not text_to_analyse or text_to_analyse.strip() == '':
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=myobj, headers=header)
    
    response_json = json.loads(response.text)
    emotions = response_json['emotionPredict']['document']['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': dominant_emotion
    }
