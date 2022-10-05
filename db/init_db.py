from sqlalchemy.orm import Session

from .base_class import Base
from .session import engine

def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)
