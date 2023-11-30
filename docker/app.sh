#!/bin/bash

poetry run alembic upgrade heads

poetry run gunicorn app.src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000