from fastapi import FastAPI, Depends
from models import UserCreate, UserOut
from auth import register_user

app = FastAPI()

@app.post("/register", response_model=UserOut)
async def register(user: UserCreate):
    return await register_user(user)
@app.get("/")
def read_root():
    return {"message":"hi deploy ho gya jy! Hurraahh"}