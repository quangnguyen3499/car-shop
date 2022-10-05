from fastapi import APIRouter

from app import cars, brands

api_router = APIRouter()
api_router.include_router(cars.router, prefix="/cars", tags=["cars"])
api_router.include_router(brands.router, prefix="/brands", tags=["brands"])
