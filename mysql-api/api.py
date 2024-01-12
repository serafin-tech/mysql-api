import logging

from fastapi import FastAPI, HTTPException
from decouple import config

from db import MySQLInterface

MYSQL_HOST = config('MYSQL_HOST', default='127.0.0.1')
MYSQL_PORT = config('MYSQL_PORT', default=3306, cast=int)
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASS = config('MYSQL_PASS')
MYSQL_DATABASE = config('MYSQL_DATABASE')

DEBUG = config('DEBUG', default=False, cast=bool)

# logging setup
logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

app = FastAPI()


@app.get("/status")
def root():
    try:
        db = MySQLInterface(MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DATABASE, MYSQL_PORT)
        db.connect()

        return {"message": "OK"}
    except RuntimeError as exception:
        logging.debug(msg=str(exception))
        raise HTTPException(status_code=502, detail='API error') from exception


@app.get("/table/{table_name}")
def table(table_name: str):
    try:
        db = MySQLInterface(MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DATABASE, MYSQL_PORT)
        db.connect()

        return db.query_full_table(table=table_name)
    except RuntimeError as exception:
        logging.debug(msg=str(exception))
        raise HTTPException(status_code=502, detail='API error') from exception
