from fastapi import APIRouter ,HTTPException,status
from src.books.bookJson import books
from src.books.schemas import bookResponse
from uuid import UUID

book_router=APIRouter()

@book_router.get('/',response_model=bookResponse,status_code=status.HTTP_200_OK)
async def getbook():    
    return 