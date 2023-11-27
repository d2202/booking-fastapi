from sqlalchemy.orm import relationship

from app.src.models.db import Base
from sqlalchemy import Column, String, Boolean


class Users(Base):
    __tablename__ = "users"

    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    booking = relationship("Bookings", back_populates="user")

    def __str__(self):
        return f"User {self.email}"
