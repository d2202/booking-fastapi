from sqladmin import ModelView

from app.src.models.bookings import Bookings
from app.src.models.hotels import Hotels
from app.src.models.rooms import Rooms
from app.src.models.users import Users


# admin models View


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email, Users.is_admin]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class BookingsAdmin(ModelView, model=Bookings):
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user]
    name = "Booking"
    name_plural = "Bookings"
    icon = "fa-solid fa-book"


class HotelsAdmin(ModelView, model=Hotels):
    column_list = [c.name for c in Hotels.__table__.c]
    name = "Hotel"
    name_plural = "Hotels"
    icon = "fa-solid fa-hotel"


class RoomsAdmin(ModelView, model=Rooms):
    column_list = [c.name for c in Rooms.__table__.c]
    name = "Room"
    name_plural = "Rooms"
    icon = "fa-solid fa-bed"
