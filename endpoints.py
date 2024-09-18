import datetime
from database import collection
from bson import ObjectId

from fastapi import APIRouter, HTTPException
from models import StudentData, StudentUpdate
from schemes import decode, data

router = APIRouter()


@router.get("/student_info/{_id}")
def student_info(_id: str):
    info = collection.find_one({"_id": ObjectId(_id)})
    decoded_data = data(info)
    return {
        "status": "Ok",
        "data": decoded_data
    }


@router.get("/student_info")
def student_info():
    info = collection.find()
    decoded_data = decode(info)

    return {
        "status": "Ok",
        "data": decoded_data
    }


@router.post("/register")
def reg_student(info: StudentData):
    info = dict(info)

    current_date = datetime.datetime.now()
    info["date_of_register"] = current_date.strftime("%m/%d/%Y")

    sdt_data = collection.insert_one(info)
    info_id = str(sdt_data.inserted_id)

    if not info["studentID"].isdigit():
        raise HTTPException(status_code=400, detail="Student ID must be numeric")

    valid_id = collection.find_one({"studentID": info["studentID"]})
    if not valid_id:
        raise HTTPException(status_code=400, detail="Invalid student ID")

    if not info["age"].isdigit():
        raise HTTPException(status_code=400, detail="Student age must be numeric")

    age = int(info["age"])
    if age > 50:
        raise HTTPException(status_code=400, detail="Invalid age")
    return {
        "status": "Ok",
        "message": "Register successfully!",
        "_id": info_id
    }


@router.patch("/student_info_update/{_id}")
def update_student(_id: str, info: StudentUpdate):
    info = dict(info.model_dump(exclude_unset=True))
    collection.update_one({"_id": ObjectId(_id)}, {"$set": info})

    return {
        "status": "Ok",
        "message": "Updated successfully!",
    }


@router.delete("/student_info_delete/{_id}")
def delete_student(_id: str):
    collection.delete_one({"_id": ObjectId(_id)})

    return {
        "status": "Ok",
        "message": "Deleted successfully!",
    }
