from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.schemas import UserCreate, UserUpdate, UserResponse
from app import crud
from app.auth import authenticate

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    _: str = Depends(authenticate)
):
    return crud.create_user(db, user.username, user.email)

@app.get("/users", response_model=list[UserResponse])
def read_users(
    db: Session = Depends(get_db),
    _: str = Depends(authenticate)
):
    return crud.get_users(db)

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(authenticate)
):
    return crud.update_user(db, user_id, user.email)

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: str = Depends(authenticate)
):
    crud.delete_user(db, user_id)
    return {"message": "User deleted successfully"}

@app.get("/")
def root():
    return {"message": "Hello, I am alive"}


