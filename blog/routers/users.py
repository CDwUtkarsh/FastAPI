from fastapi import APIRouter, Depends, status, HTTPException, Response
from blog import models, schemas
from sqlalchemy.orm import Session
from blog.database import get_db
from ..repository import users



router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/", response_model=schemas.ShowUser)
def create(request:schemas.User,db: Session = Depends(get_db)):
    return users.create(request,db) 


@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id,db: Session = Depends(get_db)):
    return users.show(id,db)
