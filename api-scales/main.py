from fastapi import FastAPI, Depends, HTTPException, Path
from db.connnector import get_table 

app = FastAPI()

@app.get('/')
def main_route():
    return {"API-STATE": "WORKS"}

@app.get('/table/{table}', response_model=list[list[str]])
async def get_table_endpoint(table: str = Depends(get_table)):
    if table is None:
        raise HTTPException(status_code=404, detail=f'The table "{table}" is empty')
    return table

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)