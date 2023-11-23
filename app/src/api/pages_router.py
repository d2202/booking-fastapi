from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.src.api.hotels_router import get_hotels

router = APIRouter(prefix="/pages", tags=["Frontend"])

templates = Jinja2Templates(directory="app/src/templates")


@router.get("/hotels")
async def get_hotels_page(request: Request, hotels_data=Depends(get_hotels)):
    try:
        data = hotels_data.hotels
    except AttributeError:
        # using cached redis data
        data = hotels_data['hotels']

    return templates.TemplateResponse(
        name="hotels.html", context={"request": request, "hotels": data}
    )
