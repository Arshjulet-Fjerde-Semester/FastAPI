

from fastapi import FastAPI
import pandas as pd
from pathlib import Path

app = FastAPI()

@app.get("/files/{file_path}")
async def return_Pdf(file_path: str):
    base_path = Path(__file__).parent
    substring = base_path.resolve()
    print(base_path)
    files_path = (substring / "/FastAPI/Files/Wöldike_1set.pdf").resolve() 
    
    files = {"file": open(files_path, 'rb').read().decode(encoding='utf-8', errors='ignore')}
    
    return files

