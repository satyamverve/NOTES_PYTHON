from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List
from sqlalchemy.orm import Session

import models

from database import engine, get_db, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

class Book(BookCreate):
    id: UUID = Field(default_factory=uuid4, alias="_id")

# READ
@app.get("/books/", response_model=List[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

# CREATE
@app.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())  # Use book.dict() instead of model_dump()
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# READ
@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: UUID, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book

# UPDATE
@app.put("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
def update_book(book_id: UUID, updated_book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    for field, value in updated_book.dict(exclude_unset=True).items():  # Use dict() instead of model_dump()
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book

# DELETE
@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: UUID, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    db.delete(db_book)
    db.commit()

    return {"message": "Book deleted successfully"}
