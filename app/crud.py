from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import User
from fastapi import HTTPException
import pymysql

def create_user(db: Session, username: str, email: str):
    user = User(username=username, email=email)
    db.add(user)

    try:
        db.commit()
        db.refresh(user)
        return user

    except (IntegrityError, pymysql.err.IntegrityError):
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, email: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.email = email
    db.commit()
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
