"""
Pydantic - Data Validation and Parsing Library

Description:
    Pydantic is a data validation and data parsing library for Python. 
    It ensures that the data you work with is correct, structured, and type-safe.

Key Concepts:
    1. Basic example
    2. Default values - Set default values for model fields
    3. Optional fields - Make fields optional with Optional type hint
    4. Coerce - Convert/coerce data to correct types
    5. Built-in validation - Automatic type checking and validation
       - Additional validations sunch as email validation
    6. Field Function - Allows:
       - Setting default values
       - Adding constraints
       - Adding descriptions
       - Using regex expressions for validation
    7. Pydantic object - Returns a Pydantic model object
       - Convert to JSON using .model_dump_json()
       - Convert to dict using .model_dump()
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    surname: str = 'Singh' # default value can be provided
    age: Optional[int] = None  # Optional imported from typing
    email:EmailStr # EmailStr imported from pydantic for validation
    cgpa: float = Field(gt=0,lt=10) # Field level validation in pydantic using Field import , description , Regex can also be added

new_student = {
    'name':'happy',
    'email':'hellobro@gmail.com',
    'cgpa':'5' # this string would automatically converted to string using pydantic
               }

"""
Dictionary Unpacking Operator (**)

The double asterisk (**) is the dictionary unpacking operator in Python.
When you write Student(**new_student), it takes the dictionary new_student 
and unpacks its key-value pairs, passing them as keyword arguments to the 
Student class constructor.

Example:
    new_student = {'name': 'happy', 'email': 'hellobro@gmail.com'}
    student = Student(**new_student)
    
    # This is equivalent to:
    student = Student(name='happy', email='hellobro@gmail.com')
"""
student = Student(**new_student)
print(student)
print(type(student))

# Pydantic object can be converted to dictionary, json

