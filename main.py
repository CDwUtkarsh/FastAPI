from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}


@app.get('/blog/unplublished')
def unpublished():
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}')
def show(id:int): 
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id:int):
    return {'data': {'1', '2'}}