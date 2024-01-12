FROM python:3.11-slim-bookworm

LABEL authors="serafin.tech"

WORKDIR /packages

COPY ./dist/*.whl /packages

RUN pip install --no-cache-dir /packages/*.whl

CMD ["uvicorn", "mysql_api.api:app", "--host", "0.0.0.0", "--port", "8080"]
