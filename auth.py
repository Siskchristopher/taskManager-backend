from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Security
from fastapi.security import OAuth2PasswordBearer


secret_key = "super_secret_key"
Algorithm = "HS256"
access_token_expire_minutes = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user_from_token(token: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[Algorithm])
        username: str = payload.get("sub")

        if username is None:
            return None
        return username
    except JWTError:
        return None

def create_access_token(data: dict):
    # Copy of data
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=Algorithm)
    return encoded_jwt

# hashing engine setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password : str):
    # converts str --> hash
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    # compare str password --> hash
    return pwd_context.verify(plain_password, hashed_password)


