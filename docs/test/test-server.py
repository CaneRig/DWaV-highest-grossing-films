from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import json

app = FastAPI()

@app.get("/index.html", response_class=HTMLResponse)
async def index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/films.json", response_class=JSONResponse)
async def get_films():
    with open("films.json", "r", encoding="utf-8") as f:
        return json.load(f) 