import speech_recognition as sr 

from fastapi import FastAPI, File, UploadFile


app = FastAPI()

recognizer = sr.Recognizer()

#model = Model("/app/stt/model/vosk-model-small-ru-0.22/")


@app.post('/recongnize')
async def recognize(file: UploadFile = File(...)):
    audio_file = sr.AudioFile(file.file)    

    with audio_file as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.record(source)
        output = recognizer.recognize_google(audio, language="ru-RU")

        return {"text": output}
 


#@app.post("/vosk")
#async def recognize_speech(file: UploadFile = File(...)):    
#    recon = ""
    
#    if file.content_type.startswith("audio/"):
#        wf = wave.open(file.file, "rb")
#        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
#            return {"error": "Audio file format not supported"}

#        rec = vosk.KaldiRecognizer(model, wf.getframerate())

#        while True:
#            data = wf.readframes(4000)
#            if len(data) == 0:
#                break
#            if rec.AcceptWaveform(data):
#                recon += rec.Result()

#        json_object = json.loads(recon)
#        return json_object
#    else:
#        return {"error": "Unsupported file format"}
