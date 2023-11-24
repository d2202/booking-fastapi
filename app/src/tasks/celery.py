from celery import Celery
from app.config import settings

# TODO: into docker or smth:
'''
1) celery -A app.src.tasks.celery:celery worker --loglevel=INFO

2) celery -A app.src.tasks.celery:celery flower   
'''

celery = Celery(
    main="tasks",
    broker=settings.BROKER_URL,
    include=["app.src.tasks.tasks"],
)
