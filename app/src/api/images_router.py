from fastapi import UploadFile, APIRouter, Response, status
import shutil


router = APIRouter(prefix="/images", tags=["Images upload"])


@router.post("/hotels")
async def post_add_hotel_image(name: int, file: UploadFile) -> Response:
    with open(f"app/src/static/images/{name}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return Response(status_code=status.HTTP_201_CREATED)
