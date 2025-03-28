from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://maria:1234567@localhost:27018/?authMechanism=DEFAULT")
db = client["tasques_db"]
