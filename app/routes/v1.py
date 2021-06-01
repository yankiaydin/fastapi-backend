from fastapi import APIRouter, Body, File, UploadFile, Response
from app.models.personel import Personel
from app.utils.db_functions import add_staff
from app.utils.photo_upload import upload_to_server

app_v1 = APIRouter()

@app_v1.post("/personel/new")
async def insert_new_personel(staff: Personel = Body(...,embed=True)):
    await add_staff(staff)
    return {"Message":"You got it"}

@app_v1.post("/files")
async def create_file(response: Response, file: bytes = File(...)):
    await upload_to_server(file)
    return {"file_size": len(file)}

@app_v1.post("/photo")
async def upload_photo(file: UploadFile = File(...)):
    return {"filename":file.filename}




