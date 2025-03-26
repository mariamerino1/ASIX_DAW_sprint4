from pydantic import BaseModel

class Tasca(BaseModel):
    title: str
    description: str
