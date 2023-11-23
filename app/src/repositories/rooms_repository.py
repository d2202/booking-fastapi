from app.src.models.rooms import Rooms
from app.src.repositories.base_repository import BaseRepository


class RoomsRepository(BaseRepository):
    model = Rooms


rooms_repository = RoomsRepository()
