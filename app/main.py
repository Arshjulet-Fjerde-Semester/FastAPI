
import py_compile
import uvicorn
from fastapi import FastAPI
import pandas as pd
import PyPDF2
from pathlib import Path

app = FastAPI()

@app.get("/files/{file_path}")
async def return_Pdf(file_path: str):
    base_path = Path(__file__).parent
    #substring to docker
    # substring = base_path.resolve()
    #files_path = (substring / "/FastAPI/Files/Wöldike_1set.pdf").resolve() 
    files_path = (base_path / "../Files/Wöldike_1set.pdf").resolve() 
    
    files = {"file": open(files_path, 'rb').read().decode(encoding='utf-8', errors='ignore')}
    
    return files

