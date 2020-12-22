from fastapi import APIRouter, HTTPException

from ..databases import manager
from ..models.casts import CastOut, CastIn

casts = APIRouter()


@casts.post("/", response_model=CastOut, status_code=201)
async def create_cast(payload: CastIn):
    cast_id = await manager.add_cast(payload)

    response = {"id": cast_id, **payload.dict()}

    return response


@casts.get("/{id}/", response_model=CastOut)
async def get_cast(cast_id: int):
    cast = await manager.get_cast(cast_id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return cast
