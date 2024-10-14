import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv()
origin = os.getenv("ORIGIN", "http://127.0.0.1:5500")
origins = [ origin ]
print(f"Allowed origins: {origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def status() -> dict:
    return {"status": "ok"}