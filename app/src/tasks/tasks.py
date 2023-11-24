from app.config import settings
from app.src.tasks.celery import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_picture(path: str) -> None:
    image_path = Path(path)
    image = Image.open(image_path)
    image_resized_basic = image.resize((1000, 500))
    image_resized_min = image.resize((200, 100))
    image_resized_basic.save(f"{settings.PATH_TO_STATIC}/images/resized_1000_500_{image_path.name}")
    image_resized_min.save(f"{settings.PATH_TO_STATIC}/images/resized_200_100_{image_path.name}")
