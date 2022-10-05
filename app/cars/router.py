from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas
from app import deps
from app.cars.service import car_model

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
    car_models = car_model.get_list(db, skip=skip, limit=limit)
    return car_models


@router.post("/", response_model=schemas.CarModel)
def create_car_model(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.CarModelCreate,
) -> Any:
    """
    Create new car model.
    """
    car_model = car_model.create(db=db, obj_in=item_in)
    return car_model


@router.put("/{id}", response_model=schemas.CarModel)
def update_car_model(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    item_in: schemas.CarModelUpdate,
) -> Any:
    """
    Update an car model.
    """
    car_model = car_model.get(db=db, id=id)
    if not car_model:
        raise HTTPException(status_code=404, detail="Car model not found")
    data = car_model.update(db=db, db_obj=car_model, obj_in=item_in)
    return data


@router.get("/{id}", response_model=schemas.CarModel)
def read_car_model(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get car model by ID.
    """
    car_model = car_model.get(db=db, id=id)
    if not car_model:
        raise HTTPException(status_code=404, detail="Car model not found")
    return car_model


@router.delete("/{id}", response_model=schemas.CarModel)
def delete_car_model(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an car model.
    """
    car_model = car_model.get(db=db, id=id)
    if not car_model:
        raise HTTPException(status_code=404, detail="Item not found")
    data = car_model.remove(db=db, id=id)
    return data
