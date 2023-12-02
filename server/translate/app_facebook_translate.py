from transformers import FSMTForConditionalGeneration, FSMTTokenizer
from fastapi import FastAPI

app = FastAPI()

model_path = "/app/translate/model/wmt19-ru-en"
tokenizer = FSMTTokenizer.from_pretrained(model_path)
model_trans = FSMTForConditionalGeneration.from_pretrained(model_path)


@app.post("/translate")
async def translate(text):
    print('start')
    input_eds = tokenizer.encode(text, return_tensors="pt")
    print('encoded')
    outputs = model_trans.generate(input_eds)
    print('generated')
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print('decoded')

    return decoded