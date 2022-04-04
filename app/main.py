import base64
from fastapi import FastAPI
import pandas as pd
from fastapi import FastAPI, WebSocket
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/files", status_code=200)
async def return_Pdf():


    base_path = Path(__file__).parent
    #substring to docker
    # substring = base_path.resolve()
    #files_path = (substring / "/FastAPI/Files/Wöldike_1set.pdf").resolve() 
    files_path = (base_path / "../app/Files/Wöldike_1set.pdf").resolve() 
    
    
    return await base64.b64encode(open(files_path, 'rb').read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # while True:
        #data = await websocket.receive_text()
    base_path = Path(__file__).parent
    files_path = (base_path / "../Files/Wöldike_1set.pdf").resolve()
    await websocket.send_bytes(open(files_path, 'rb').read())
