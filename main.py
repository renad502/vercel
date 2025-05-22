from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def health_check():
    return {"message": "The health check is successful"}

handler = Mangum(app)
