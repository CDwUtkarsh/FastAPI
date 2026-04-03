from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def index():
    return {"data": "Welcome to FastAPI"}

@app.get("/about")
def about():
    return {"data": "This is about page"}

@app.get("/contact")
def contact():
    return {"data": "Contact us"}

@app.get("/user")
def get_user():
    return {
        "name": "Utkarsh",
        "age": 21,
        "Skills": ["Python", "FastAPI"]
    }

@app.get("/item/{item_id}")
def get_item(item_id : int):
    return {"item_id": item_id}

@app.get("/hello/{name}")
def get_name(name : str):
    return {"name": f"hello {name}"}

@app.get("/product/{id}")
def get_product(id : int):
    return {"id": id,"name": "Sample Product"}

@app.get("/search")
def search(q:str):
    return {"query": q}


@app.get("/filter")
def filter(c :str,p:int):
    return {"category": c,"price":p}

@app.get("/items")
def get_items(limit:int = 10):
    return {"limit":limit}


items = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

@app.get("/items/{id}")
def get_item(id: int):
    for item in items:
        if item["id"] == id:
            return item
    return {"error": "Item not found"}

  