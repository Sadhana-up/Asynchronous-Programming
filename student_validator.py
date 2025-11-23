from pydantic import Field,ValidationError,EmailStr,BaseModel,model_validator,field_validator,field_serializer
from typing import Annotated

class Students(BaseModel):
    fullname : str = Field(max_length=30 , min_length=5)
    email : EmailStr 
    marks : int = Field(ge=0,le=100)
    grade : int | str 
    location : str = None 


    @model_validator(mode='before')
    
    def normalize_name(cls,value):
        if "fullname" in value and isinstance(value["fullname"],str):
            value["fullname"] = value["fullname"].title().strip() # spaces hatako  ra capitalize gareko cause we r recieving as a dict

        if "grade" in value and isinstance(value["grade"],str):
            value["grade"]= value["grade"].upper().strip()

        return value
    
        
# s1 = Students(fullname="sadhana
data = {
    "fullname": "  john doe  ",
    "email": "john@example.com",
    "marks": 85,
    "grade": "a"
}

s1 = Students(**data)
print(s1.fullname)





