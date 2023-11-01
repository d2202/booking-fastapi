from app.db import Base
from sqlalchemy import Column, Date, DECIMAL, ForeignKey, Computed


class Bookings(Base):
    __tablename__ = "bookings"

    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    total_cost = Column(DECIMAL(10, 2), Computed("(date_to - date_from) * price"))
    total_days = Column(DECIMAL(10, 2), Computed("date_to - date_from"))
