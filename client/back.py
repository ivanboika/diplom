import requests


def recognize_speech(audio_file):
    with open(audio_file, 'rb') as file:
        files = {'file': (audio_file, file, 'audio/wav')}  # Имя файла, файл, тип содержимого
        response = requests.post("http://127.0.0.1:8000/recongnize", files=files)
        return response.json()


def translate(text):
    payload = {'text': text}
    response = requests.post("http://127.0.0.1:8001/translate", params=payload)
    return response.text
