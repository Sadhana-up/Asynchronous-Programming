from pydantic import ValidationError

class sstudent_validator():
    def __init__(self,model):
        self.model = model 
    

    def validate_row(self, row: dict):
        try:
            student = self.model(**row)
            return student, None
        except ValidationError as e:
            return None, e.errors()