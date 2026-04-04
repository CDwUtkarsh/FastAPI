from fastapi import FastAPI
from . import  models
from .database import engine
from .routers import blog, users, authentication


app =FastAPI()

models.Base.metadata.create_all(engine)  #TO Create TABLE in SQLite

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(users.router)





