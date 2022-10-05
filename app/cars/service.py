from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.base import APIBase
from .models import CarModel
from schemas.car_model import CarModelCreate, CarModelUpdate


class ServiceCarModel(APIBase[CarModel, CarModelCreate, CarModelUpdate]):
    def create(
        self, db: Session, *, obj_in: CarModelCreate
    ) -> CarModel:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_list(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[CarModel]:
        return (
            # db.query(self.model)
            # # .filter(CarModel.owner_id == owner_id)
            # .offset(skip)
            # .limit(limit)
            # .all()
            db.query(CarModel).all()
        )


car_model = ServiceCarModel(CarModel)
