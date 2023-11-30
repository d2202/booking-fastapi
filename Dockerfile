FROM python:3.11

RUN pip install poetry==1.2.2

RUN mkdir /booking

WORKDIR /booking

COPY . .

RUN poetry install

RUN chmod a+x /booking/docker/*.sh

CMD ["poetry", "run", "gunicorn", "app.src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
