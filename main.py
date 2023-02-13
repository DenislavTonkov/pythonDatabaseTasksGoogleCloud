from fastapi import FastAPI

from sqlite_inserting_data import total_sales_per_customer

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/totalsales")
def read_root():
    return {"Hello": "World"}

