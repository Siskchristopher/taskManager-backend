from passlib.context import CryptContext

# hashing engine setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password : str):
    # converts str --> hash
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    # compare str password --> hash
    return pwd_context.verify(plain_password, hashed_password)


