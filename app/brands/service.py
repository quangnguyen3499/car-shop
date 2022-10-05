from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.base import APIBase
from .models import CarBrand
from schemas.car_brand import CarBrandCreate, CarBrandUpdate


class ServiceCarBrand(APIBase[CarBrand, CarBrandCreate, CarBrandUpdate]):
    def create(
        self, db: Session, *, obj_in: CarBrandCreate
    ) -> CarBrand:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_list(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[CarBrand]:
        return (
            db.query(self.model)
            # .filter(Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


car_brand = ServiceCarBrand(CarBrand)
