from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gateway.ollama_client import generate_text

import os

app = FastAPI(title="LLM Gateway")

MODEL_NAME = os.getenv("MODEL_NAME", "tinyllama")


class GenerateRequest(BaseModel):
    prompt: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model": MODEL_NAME
    }


@app.get("/model")
def model_info():
    return {
        "model": MODEL_NAME
    }


@app.post("/generate")
def generate(req: GenerateRequest):
    try:
        output = generate_text(req.prompt)
        return {"response": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
