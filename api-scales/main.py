
import pymongo 
from db.connnector import get_table as mysql_get_table

from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def main_route():
    return {"API-STATE" : "WORKS"}

@app.get('/table/items')
async def get_table():
    return mysql_get_table('items')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)