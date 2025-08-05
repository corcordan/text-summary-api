from typing import Union, Optional
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.get("/")
def root():
    return {"Hello" : "World"}

@app.post("/summarize")
def summarize(text: str):
    if len(text.strip()) > 0:
        return summarizer(text, max_length=10, min_length=5, do_sample=False)
    else:
        raise HTTPException(status_code=400, detail="Input text must not be empty.")