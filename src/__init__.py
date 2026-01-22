from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is started")

    yield

    print("Server is stopped")


version = "v1"
app = FastAPI(
    title=" Bookley", version=version, description="Bookley", lifespan=lifespan
) 

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
