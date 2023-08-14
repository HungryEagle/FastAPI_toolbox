from fastapi import FastAPI
from toolbox import hello

app = FastAPI()
app.include_router(hello.router)


@app.get("/")
async def root():
    return {"thought": "Hello from FastAPI toolbox"}
