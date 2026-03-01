from fastapi import FastAPI
from db import Database

app = FastAPI()
db = Database("./corkboard/data/db.db")

@app.get("/")
async def root():
    return {"message": "You've found an instance of corkboard, a single-file image hosting service built with FastAPI!"}

@app.get("/{id}")
async def show(id):
    
    return {"success": id}

@app.post("/upload")
async def upload(img_data):
    # upload picture to server and create id
    # this wasnt implemented because its almost 11 PM
    return {"id": uploaded.id}

# welp i'll see you in a few days, that's my entire commit for now.
