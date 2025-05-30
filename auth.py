from passlib.context import CryptContext
from bson import ObjectId
from database import users_collection
from models import UserCreate, UserOut
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def register_user(user: UserCreate) -> UserOut:
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_pwd

    result = await users_collection.insert_one(user_dict)
    return UserOut(id=str(result.inserted_id), name=user.name, email=user.email)
