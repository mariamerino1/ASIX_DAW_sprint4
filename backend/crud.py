from database import db
from models import Tasca
from bson import ObjectId

collection = db["tasques"]

def tasca_helper(tasca) -> dict:
    return {
        "id": str(tasca["_id"]),
        "title": tasca["title"],
        "description": tasca["description"]
    }

async def get_all_tasques():
    return [tasca_helper(t) async for t in collection.find()]

async def create_tasca(tasca: Tasca):
    result = await collection.insert_one(tasca.dict())
    return await collection.find_one({"_id": result.inserted_id})

async def delete_tasca(id: str):
    return await collection.delete_one({"_id": ObjectId(id)})

async def update_tasca(id: str, tasca: Tasca):
    await collection.update_one({"_id": ObjectId(id)}, {"$set": tasca.dict()})
    return await collection.find_one({"_id": ObjectId(id)})
