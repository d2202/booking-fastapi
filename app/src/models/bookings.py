from sqlalchemy.orm import relationship

from app.src.models.db import Base
from sqlalchemy import Column, Date, DECIMAL, ForeignKey, Computed, Integer


class Bookings(Base):
    __tablename__ = "bookings"

    room_id = Column(ForeignKey("rooms.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    total_cost = Column(
        DECIMAL(10, 2), Computed("(date_to - date_from) * price"), nullable=False
    )
    total_days = Column(Integer, Computed("date_to - date_from"), nullable=False)

    user = relationship("Users", back_populates="booking")
    room = relationship("Rooms", back_populates="booking")

    def __str__(self):
        return f"Booking {self.id}"
