from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.personel import Personel
from utils.db_functions import fetch_staff, login_staff
from routes.v1 import app_v1
from routes.v2 import app_v2
from starlette.status import HTTP_401_UNAUTHORIZED
from utils.security import create_jwt_token, authenticate_user, check_jwt_token
import jwt
import time
from utils.db_object import db
import utils.redis_object as re
import aioredis
from utils.const import REDIS_URL
from utils.redis_object import check_redis_status

app = FastAPI(
    title="Database for the HR Department",
    description="It is an API which is used for to collect employess data",
    version="1.2.0",
)
app.include_router(
    app_v1,
    prefix="/v1",
    dependencies=[Depends(check_jwt_token), Depends(check_redis_status)],
)
app.include_router(
    app_v2,
    prefix="/v2",
    dependencies=[Depends(check_jwt_token), Depends(check_redis_status)],
)


@app.on_event("startup")
async def connect_db():
    await db.connect()
    # re.redis = await aioredis.create_redis_pool(REDIS_URL)


@app.on_event("shutdown")
async def disconnect_db():
    await db.disconnect()
    # re.redis.close()
    # await re.redis.wait_closed()


@app.get("/")
async def main_page():
    return {"Message": "This is Fastapi"}


@app.post("/token")
async def jwt_token(form_data: OAuth2PasswordRequestForm = Depends()):
    data = {"name": form_data.username, "password": form_data.password}
    staff = Personel(**data)
    result = await authenticate_user(staff)
    if result is None:
        raise HTTPException(HTTP_401_UNAUTHORIZED)
    query = await create_jwt_token(staff)
    return {"acces_token": query}


@app.get("/personel/{position}")
async def get_user_by_position(position: str):
    data = await fetch_staff(position)
    return {"result": data}


@app.post("/personel/login")
async def login_as_personel(persona: Personel):
    result = await login_staff(persona)
    if result is None:
        return {"Message": "Denied"}
    return {"is_valid(db)": "Succesfully entered"}


@app.post("/personel")
async def signed_up(person: Personel, jwt: bool = Depends(check_jwt_token)):
    return {"User is": person}


@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-process-Time"] = str(process_time)
    return response
