from app.src.models.db import Base
from sqlalchemy import Column, String, Integer, DECIMAL, JSON, ForeignKey


class Rooms(Base):
    __tablename__ = "rooms"

    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(DECIMAL(10, 2), nullable=False)
    services = Column(JSON)
    quantity = Column(Integer, nullable=False, default=1)
    image_id = Column(Integer)
