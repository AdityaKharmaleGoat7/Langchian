'''
Pydantic is a data validation and
data parsing library for Python, which is used to define data models
with type annotations. It is often used in conjunction with frameworks like FastAPI
and Django for data validation and serialization.
'''

from pydantic import BaseModel, EmailStr, Field
from typing import Optional



class Student(BaseModel):
    name: str = "Aditya Kharmale"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {'age':2, 'email': 'abc@gmail.com', 'cgpa': 9.5} 

student = Student(**new_student)
print(student)  