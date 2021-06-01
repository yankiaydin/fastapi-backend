from fastapi import APIRouter, Body
from app.models.personel import Personel
from app.utils.db_functions import patch_position, delete_staff, update_staff


app_v2 = APIRouter()

@app_v2.delete("/personel/delete/{id}")
async def delete_personel_by_id(id: int):
    await delete_staff(id)
    return {"Message":"Personel deleted"}


@app_v2.put("/personel/feature/{id}")
async def update_personel_by_id(id: int, persona: Personel = Body(...,embed=True)):
    await update_staff(id, persona)
    return {"Message":"Succesfull updated"}

@app_v2.patch("/personel/position/{id}")
async def patch_user_by_id(id : int, position: str):
    await patch_position(id, position)
    return {"Message":"Position of the personel is succesfully updated"}

@app_v2.patch("/personel/{position}")
async def deneme(person : Personel, position: str):
    person.position = position
    return {"yeni görev": person}
