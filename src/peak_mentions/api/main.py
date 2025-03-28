from fastapi import FastAPI
from src.peak_mentions.api.endpoints import facebook, x, reddit

app = FastAPI()

app.include_router(facebook.router)
app.include_router(x.router)
app.include_router(reddit.router)