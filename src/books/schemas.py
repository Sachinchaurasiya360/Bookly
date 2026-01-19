from pydantic import BaseModel

class bookData(BaseModel):
    title:str | None
    description:str
    price:int
    rating:int
    
class bookResponse(BaseModel):
    id:int
    title:str
    