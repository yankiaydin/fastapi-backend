from passlib.context import CryptContext
from app.utils.const import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.models.personel import Personel
import jwt
from fastapi import Depends, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime
import time
from app.utils.db_functions import login_staff

pwd_context = CryptContext(schemes=["bcrypt"])
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")

fake_db = [{"name":"sergen","password":"$2b$12$4kTtdjI3HpZ48VZzLZ8sW.ESqnHakHNoqLHjReMJBUiaDj8BF.IY6","position":"manager","department":None,"id":10},
           {"name":"mehmet","password":"secret","position":"manager","department":None,"id":12}]
fake_user = {"name":"sergen","password":"$2b$12$4kTtdjI3HpZ48VZzLZ8sW.ESqnHakHNoqLHjReMJBUiaDj8BF.IY6","position":"manager","department":None,"id":10}
fake_class = Personel(**fake_user)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate_user(person1):
    result = await login_staff(person1)
    if result is None:
        return None
    return True

async def create_jwt_token(person1 : Personel):
    exp_time = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    jwt_payload = {
        "sub": person1.name,
        "password": person1.password,
        "exp": exp_time
    }
    encoded_jwt = jwt.encode(jwt_payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"acces_token is": encoded_jwt}

async def check_jwt_token(encoded_jwt : str = Depends(oauth_schema)):
    try:
        decoded_token = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=ALGORITHM)
        name = decoded_token.get("sub")
        expiration = decoded_token.get("exp")
        if expiration > time.time():
            if fake_class.name == name:
                return True
    except Exception as e:
        raise HTTPException(HTTP_401_UNAUTHORIZED)

    raise HTTPException(HTTP_401_UNAUTHORIZED)


