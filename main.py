
import py_compile
import uvicorn
from fastapi import FastAPI
import pandas as pd
import PyPDF2

app = FastAPI()

@app.get("/files/{file_path:path}")
async def return_Pdf(file_path: str):
    #Creating an pdf obj
    pdfFileObj = open('Files/sample.pdf' , 'rb')
    #createing an pdf reader obj
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader)
    #creating page obj
    pageObj = pdfReader.getPage(0)

    
    return pageObj