# Emotion Detector

AI-based web application for detecting emotions from text using Watson NLP library.

## Features
- Emotion detection using Watson NLP
- REST API with Flask
- Support for emotions: anger, disgust, fear, joy, sadness
- Error handling for blank input
- Unit testing included
- Static code analysis compliance

## Installation
```bash
pip install requests flask
```

## Usage
```python
from EmotionDetection.emotion_detection import emotion_detector
result = emotion_detector("I am happy")
print(result)
```

## Project Structure
- EmotionDetection/: Main package
  - emotion_detection.py: Core emotion detection logic
  - __init__.py: Package initialization
- server.py: Flask server
- test_emotion_detection.py: Unit tests
