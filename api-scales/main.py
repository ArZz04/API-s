
import pymongo 
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main_route():
    return {"API-STATE" : "WORKS"}

#