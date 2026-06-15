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
    6. Field Function - Allows:
       - Setting default values
       - Adding constraints
       - Adding descriptions
       - Using regex expressions for validation
    7. Pydantic object - Returns a Pydantic model object
       - Convert to JSON using .model_dump_json()
       - Convert to dict using .model_dump()
"""

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    surname: str = 'Singh' #default value can be provided

new_student = {'name':'happy'}

student = Student(**new_student)
print(student)
print(type(student))

