from fastapi import FastAPI, Depends, HTTPException, Request, From, File, UploadFile
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from schemas import LibCreate, LibUpdate, LibOut
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from uuid import uuid4

#테이블 생성
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

#전체 목록 조회
@app.get("/books", response_model=list[LibOut])
def get_books(db:Session=Depends(get_db)):
    return db.query(models.Library).all()

#책 상세 내용 조회
@app.get("/books/{isbn}", response_model=LibOut)
def get_book(isbn:int, db:Session=Depends(get_db)):
    book = db.query(models.Library).get(isbn)
    if not book:
        raise HTTPException(404, "Not Found")
    return book

#책 추가
@app.post("/books/create", response_model=LibOut)
def create_book(book : LibCreate, db:Session = Depends(get_db)):
    db_book = models.Library(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

#책 수정
@app.post("/books/edit/{isbn}", response_model=LibOut)
def update_book(isbn:int, data:LibUpdate, db:Session = Depends(get_db)):
    book = db.query(models.Library).get(isbn)
    if not book:
        raise HTTPException(404)
    book.book_title = data.title
    book.book_author = data.author
    book.publisher = data.publisher
    db.commit()
    return book

#책 삭제
@app.post("/books/delete/{isbn}")
def delete_book(isbn: int, db:Session=Depends(get_db)):
    book = db.query(models.Library).get(isbn)
    if not book:
        raise HTTPException(404)
    db.delete(book)
    db.commit()
    return {"message":"deleted"}