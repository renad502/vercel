from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "The health check is successful"}

