def data(info) -> dict:
    return {
        "_id": str(info["_id"]),
        "name": info["name"],
        "studentID": info["studentID"],
        "age": info["age"],
        "sex": info["sex"]
    }


def decode(infos) -> list:
    return [data(info) for info in infos]
