#!/bin/bash

if [[ "${1}" == "celery" ]]; then
    poetry run celery -A app.src.tasks.celery:celery worker -l INFO
elif [[ "${1}" == "flower" ]]; then
    poetry run celery -A app.src.tasks.celery:celery flower
fi