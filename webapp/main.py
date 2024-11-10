from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

generator = pipeline('text-generation', model='gpt2')

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

class Body(BaseModel):
    text: str

@app.get('/')
def root():
    return HTMLResponse("<h1> A self-documenting API to interact with a GPT2 model and generate text</h1>")

@app.post('/generate')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results [0]

#para ejecutar: cd webapp  --> uvicorn --host 0.0.0.0 main:app
#va a cargar el link: http://localhost:8000
#ponerle así para ver el Swagger UI http://localhost:8000/docs
