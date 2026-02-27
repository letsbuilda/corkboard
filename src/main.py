from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "You've found an instance of corkboard, a single-file image hosting service built with FastAPI!"}

@app.get("/{id}")
async def show(img_id):
    # fetch image and send it to the user as raw data
    return {"success": img_id}

@app.post("/upload")
async def upload(img_data):
    # upload picture to server and create id
    # this wasnt implemented because its almost 11 PM
    return {"id": uploaded.id}

# welp i'll see you in a few days, that's my entire commit for now.
