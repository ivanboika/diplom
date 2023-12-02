import vosk
import wave
import json
import shutil
import noisereduce as nr

from vosk import Model

from datetime import datetime
from scipy.io import wavfile

from fastapi import FastAPI, File, UploadFile


app = FastAPI()

model = Model("/app/stt/model/vosk-model-small-ru-0.22/")


@app.post("/vosk")
async def recognize_speech(file: UploadFile = File(...)):    
    recon = ""
    
    if file.content_type.startswith("audio/"):
        wf = wave.open(file.file, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
            return {"error": "Audio file format not supported"}

        rec = vosk.KaldiRecognizer(model, wf.getframerate())

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                recon += rec.Result()

        json_object = json.loads(recon)
        return json_object
    else:
        return {"error": "Unsupported file format"}
