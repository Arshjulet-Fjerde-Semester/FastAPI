
import uvicorn
from fastapi import FastAPI
import pandas as pd
import gcsfs
import pandas_gbq
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}