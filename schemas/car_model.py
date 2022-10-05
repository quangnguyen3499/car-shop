from typing import Optional

from pydantic import BaseModel


# Shared properties
class CarModelBase(BaseModel):
    description: Optional[str] = None


# Properties to receive on Car model creation
class CarModelCreate(CarModelBase):
    name: str
    image_url: str
    description: str
    brand_id: int


# Properties to receive on Car model update
class CarModelUpdate(CarModelBase):
    pass


# Properties shared by models stored in DB
class CarModelInDBBase(CarModelBase):
    id: int
    name: str
    image_url: str
    description: str
    brand_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class CarModel(CarModelInDBBase):
    pass


# Properties properties stored in DB
class CarModelInDB(CarModelInDBBase):
    pass
