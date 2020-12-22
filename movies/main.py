from fastapi import FastAPI

from app.apis.movies import movies
from app.databases.movies import metadata, engine, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies, prefix="/api/v1/movies", tags=["movies"])
