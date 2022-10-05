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
    data = car_brand.create(db=db, obj_in=item_in)
    return data


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
    data = car_brand.get(db=db, id=id)
    if not data:
        raise HTTPException(status_code=404, detail="Car brand not found")
    response = car_brand.update(db=db, db_obj=data, obj_in=item_in)
    return response


@router.get("/{id}", response_model=schemas.CarBrand)
def read_car_brand(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get car brand by ID.
    """
    data = car_brand.get(db=db, id=id)
    if not data:
        raise HTTPException(status_code=404, detail="Car brand not found")
    return data


@router.delete("/{id}", response_model=schemas.CarBrand)
def delete_car_brand(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an car brand.
    """
    data = car_brand.get(db=db, id=id)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    response = car_brand.remove(db=db, id=id)
    return response
