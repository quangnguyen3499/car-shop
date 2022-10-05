from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class CarBrandBase(BaseModel):
    description: Optional[str] = None


# Properties to receive on Car brand creation
class CarBrandCreate(CarBrandBase):
    name: str
    num_of_models: int
    logo_url: str
    description: str
    status: str


# Properties to receive on Car brand update
class CarBrandUpdate(CarBrandBase):
    pass


# Properties shared by models stored in DB
class CarBrandInDBBase(CarBrandBase):
    id: int
    name: str
    num_of_models: int
    logo_url: str
    description: str
    last_update: datetime
    status: str

    class Config:
        orm_mode = True


# Properties to return to client
class CarBrand(CarBrandInDBBase):
    pass


# Properties properties stored in DB
class CarBrandInDB(CarBrandInDBBase):
    pass
