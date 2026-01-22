from pydantic import BaseModel

class Book_response(BaseModel):
    id: int
    title: str
    author:str


class Book_data_receiving_from_user(BaseModel):
    id:int
    title:str
    description:str
    author: str

class Book_update_data(BaseModel):
    title:str
    description: str
    author:str