from fastapi import APIRouter, status, HTTPException
from src.books.book_schema import Book_response, Book_data_receiving_from_user ,Book_update_data
from src.books.book_db import books

book_router = APIRouter()


@book_router.get("/", response_model=list[Book_response], status_code=200)
def get_book_response():
    return books


@book_router.post(
    "/", response_model=Book_response, status_code=status.HTTP_201_CREATED
)
def Create_book(paylod: Book_data_receiving_from_user):
    print(paylod)
    new_books = Book_data_receiving_from_user.model_dump(
        paylod
    )  # converts the Pydantic object into a normal Python dict. since user send
    books.append(new_books)
    return new_books


@book_router.get("/{bookid}")
def get_book_by_id(bookid: int):
    for isBookExist in books:
        if isBookExist["id"] == bookid:
            return isBookExist
        print(isBookExist)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="This book does not exist into the database",
    )

@book_router.patch("/{bookId}",response_model=Book_response,status_code=status.HTTP_200_OK)
def update_book_details(bookId:int, book_body:Book_update_data):
    print(book_body)
    for isBookExist in books:
        if isBookExist["id"]== bookId:
            isBookExist["title"]=book_body.title
            isBookExist["description"]= book_body.description
            isBookExist["author"]=book_body.author
            
            return isBookExist
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book id does not exist")
    
