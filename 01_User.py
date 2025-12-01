from pydantic import BaseModel,Field,field_validator,model_validator,EmailStr,ValidationError

class User(BaseModel):
    name :str 
    email: EmailStr
    monthly_budget : int
    expenses :list[int]

    @field_validator("monthly_budget")
    @classmethod
    def verification(cls,value):
        if value<=0:
            raise ValueError("Can't be less than 0 ")
        return value 
    
    def show_details(self):
        print(f"Name is  {self.name}")

    @field_validator("name")
    @classmethod
    def name_verify(cls,val):
        if not val.isalpha():
            raise ValueError("Name must only cointain leters")
        return val.title()
    
        

        

    
# #Usage 
# user1 = User(name="sadhana",email="uprety@gmail.com",monthly_budget=20,expenses=[100,200])
# user1.show_details()
