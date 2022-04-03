from typing import Optional

from fastapi import FastAPI

#create fastapi object
app = FastAPI()

#create endpoint (route)
@app.get("/")
async def root():
    return {"message": "Hello World"}

#another endpoint with parameter
@app.get("/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
