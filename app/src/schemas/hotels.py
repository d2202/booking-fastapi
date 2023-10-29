from datetime import date
from typing import Optional
from fastapi import Query


class GetHotelsRequestArgs():
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: Optional[bool],
            stars: Optional[int] = Query(default=None, ge=1, le=5),
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars
