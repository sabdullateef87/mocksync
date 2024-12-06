import os
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv();

SECRET_KEY = os.environ.get('SECRET_KEY')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)