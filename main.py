from fastapi import FastAPI

app =FastAPI()

@app.get("/hello")
async def hello():
    return {'hello':'world'}
@app.get("/hello/{name}")
async def hello_person(name:str):
    return {'hello':name}

@app.get("/")
async def hello():
    return {'hello':'home'}