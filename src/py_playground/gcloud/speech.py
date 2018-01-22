from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def recognize(filename="output.wav"):
    client = speech.SpeechClient()
    with open(filename, 'rb') as file:
        content = file.read()
        audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US')
    response = client.recognize(config, audio)
    return response


if __name__ == '__main__':
    recognize()
