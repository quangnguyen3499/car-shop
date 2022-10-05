from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
from app import deps
from app.brands.service import car_brand

router = APIRouter()

@router.get("/", response_model=List[schemas.CarModel])
def read_models(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve car models.
    """
    car_brands = car_brand.get_list(db, skip=skip, limit=limit)
    return car_brands


@router.post("/", response_model=schemas.CarBrand)
def create_car_brand(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.CarBrandCreate,
) -> Any:
    """
    Create new car brand.
    """
    car_brand = car_brand.create(db=db, obj_in=item_in)
    return car_brand


@router.put("/{id}", response_model=schemas.CarBrand)
def update_car_brand(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.CarBrandUpdate,
) -> Any:
    """
    Update an car brand.
    """
    car_brand = car_brand.get(db=db, id=id)
    if not car_brand:
        raise HTTPException(status_code=404, detail="Car brand not found")
    data = car_brand.update(db=db, db_obj=car_brand, obj_in=item_in)
    return data


@router.get("/{id}", response_model=schemas.CarBrand)
def read_car_brand(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get car brand by ID.
    """
    car_brand = car_brand.get(db=db, id=id)
    if not car_brand:
        raise HTTPException(status_code=404, detail="Car brand not found")
    return car_brand


@router.delete("/{id}", response_model=schemas.CarBrand)
def delete_car_brand(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an car brand.
    """
    car_brand = car_brand.get(db=db, id=id)
    if not car_brand:
        raise HTTPException(status_code=404, detail="Item not found")
    data = car_brand.remove(db=db, id=id)
    return data
