from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.base import APIBase
from .models import CarModel
from schemas.car_model import CarModelCreate, CarModelUpdate


class ServiceCarModel(APIBase[CarModel, CarModelCreate, CarModelUpdate]):
    def create(self, db: Session, *, obj_in: CarModelCreate) -> CarModel:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_list(
        self,
        db: Session,
        *,
        brand_id: int = 0,
        skip: int = 0,
        limit: int = 100,
        name: str,
    ) -> List[CarModel]:
        queryset = (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )
        if brand_id != 0:
            queryset = [x for x in queryset if x.brand_id == brand_id]
        if name:
            queryset = [x for x in queryset if name in x.name]
        return queryset

    # def update(
    #     self, db: Session, *, obj_in: CarModelUpdate, db_obj: CarModel,
    # ) -> CarModel:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     for key, value in obj_in_data.items():
    #         setattr(db_obj, key, value)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj


car_model = ServiceCarModel(CarModel)
