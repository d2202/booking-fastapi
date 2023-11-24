from fastapi import UploadFile, APIRouter, Response, status
import shutil

from app.config import settings
from app.src.tasks.tasks import process_picture

router = APIRouter(prefix="/images", tags=["Images upload"])


@router.post("/hotels")
async def post_add_hotel_image(name: int, file: UploadFile) -> Response:
    saving_path = f"{settings.PATH_TO_STATIC}/images/{name}.webp"
    with open(saving_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_picture.delay(path=saving_path)
    return Response(status_code=status.HTTP_201_CREATED)
