from fastapi import FastAPI
from app.api.api_v1.api import router as api_router

description = """
Ricksixty helps you access twitter api for your analytical project. 🚀

Please note that this is a work in progress.



## Users

You will be able to:

* **Get user** (you will be able to get twitter user).
* **Get followers** .
* **Get following** .
* **Get tweets** .
"""

app = FastAPI(
    title="Ricksixty",
    description=description,
    version="0.0.1",
    contact={
        "name": "bandersnatchx64",
        "url": "https://twitter.com/bandersnatchx64",
        "email": "lordareello@gmail.com",
    },
    
)


@app.get('/')
async def root():
    return {'message':'hello world'}



app.include_router(api_router, prefix='/api/v1')

