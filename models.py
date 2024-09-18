from enum import Enum

from pydantic import BaseModel, constr


class SexEnum(str, Enum):
    female = 'Female'
    male = 'Male'


class StudentData(BaseModel):
    name: str
    studentID: constr(max_length=8, min_length=8)
    age: constr(max_length=2, min_length=2)
    sex: SexEnum


class StudentUpdate(BaseModel):
    name: str = None
    studentID: int = None
    age: int = None
    sex: SexEnum = None
