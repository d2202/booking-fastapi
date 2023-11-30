from celery import Celery
from app.config import settings


celery = Celery(
    main="tasks",
    broker=settings.BROKER_URL,
    include=["app.src.tasks.tasks"],
)
