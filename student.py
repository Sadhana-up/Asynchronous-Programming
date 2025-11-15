from pydantic import Field,ValidationError,EmailStr,BaseModel
from typing import Annotated

class Students(BaseModel):
    fullname : str = Field(max_length=30 , min_length=5)
    email : EmailStr 
    marks : int = Field(ge=0,le=100)
    grade : int | str 
    location : str = None 
