import os
from dotenv import load_dotenv
from typing import Union

from fastapi import FastAPI


load_dotenv()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
