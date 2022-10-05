from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db.base import Base

class CarBrand(Base):
    __tablename__ = "car_brand"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    num_of_models = Column(Integer)
    logo_url = Column(String)
    description = Column(String)
    last_update = Column(DateTime)
    status = Column(String, index=True)
    car_models = relationship("CarModel", back_populates="car_brand")
