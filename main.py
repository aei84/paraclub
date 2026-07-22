from fastapi import FastAPI

app = FastAPI(title="ParaClub")


@app.get("/")
async def home():
    return {
        "project": "ParaClub",
        "status": "OK"
    }