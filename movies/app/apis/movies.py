from typing import List

from fastapi import APIRouter, HTTPException

from ..databases import manager
from ..models.movies import MovieIn, MovieOut, MovieUpdate
from ..services.casts import is_cast_present

movies = APIRouter()

fake_movie_db = [
    {
        "name": "Star Wars: Episode IX - The Rise of Skywalker",
        "plot": "The surviving members of the resistance face the First Order once again.",
        "genres": ["Action", "Adventure", "Fantasy"],
        "casts": ["Daisy Ridley", "Adam Driver"],
    }
]


@movies.get("/", response_model=List[MovieOut])
async def get_movies():
    return await manager.get_all_movies()


@movies.get("/{movie_id}/", response_model=MovieOut)
async def get_movie(movie_id: int):
    movie = await manager.get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@movies.post("/", status_code=201)
async def create_movie(payload: MovieIn):
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404, detail=f"Cast with id:{cast_id} not found"
            )
    movie_id = await manager.add_movie(payload)
    response = {"id": movie_id, **payload.dict()}

    return response


@movies.put("/{movie_id}/", response_model=MovieOut)
async def update_movie(movie_id: int, payload: MovieUpdate):
    movie = await manager.get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset=True)

    if "casts_id" in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(
                    status_code=404,
                    detail=f"Cast with given id:{cast_id} not found",
                )

    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await manager.update_movie(movie_id, updated_movie)


@movies.delete("/{movie_id}", response_model=None)
async def delete_movie(movie_id: int):
    movie = await manager.get_movie(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await manager.delete_movie(movie_id)
