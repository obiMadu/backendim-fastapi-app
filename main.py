from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello BackendIM"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "message": "Item details"}
