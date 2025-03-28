from fastapi import APIRouter, HTTPException
from models import Tasca
from crud import *

router = APIRouter()

@router.get("/tasques")
async def llegir_tasques():
    return await get_all_tasques()

@router.post("/tasques")
async def crear_tasca(tasca: Tasca):
    nova = await create_tasca(tasca)
    return tasca_helper(nova)

@router.put("/tasques/{id}")
async def actualitzar_tasca(id: str, tasca: Tasca):
    actualitzada = await update_tasca(id, tasca)
    return tasca_helper(actualitzada)

@router.delete("/tasques/{id}")
async def eliminar_tasca(id: str):
    result = await delete_tasca(id)
    return {"deleted": result.deleted_count == 1}
