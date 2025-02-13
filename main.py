from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/home", description="Я создал первую ручку на FastAPI", summary="Оно работает")
def root():
    return "Hello"


@app.get("/books", summary="Хранилище книг", description="Вот тут хранятся следующие книги")
def get_books():
    return books


@app.get("/books/{book_id}", summary="Получаем конкретную книгу")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book        
    raise HTTPException(status_code=404, detail="Книга не найдена")


class Book(BaseModel):
    name : str
    author : str



@app.post("/books")
def create_book(new_book: Book):
    books.append({
        "id" : len(books)+1,
        "name" : new_book.name,
        "author" : new_book.author,
    })
    return {"success" : True}



books = [
    {
        "id" : 1,
        "name" : "Золотая рыбка",
        "author" : "Пушкин А.С.",
    },
    {
        "id" : 2,
        "name" : "Мертвые души",
        "author" : "Гоголь Н.В.",
    },

    
]