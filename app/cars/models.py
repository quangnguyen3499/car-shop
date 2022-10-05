from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.brands.models import CarBrand

from db.base import Base

class CarModel(Base):
    __tablename__ = "car_model"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image_url = Column(String)
    description = Column(String)
    brand_id = Column(Integer, ForeignKey(CarBrand.id))
    car_brand = relationship("CarBrand", back_populates="car_models")
