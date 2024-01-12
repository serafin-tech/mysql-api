import logging
from typing import Dict, List

import mysql.connector


class MySQLInterface:
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

        self.cnx = None

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user=self.user,
                                               password=self.password,
                                               host=self.host,
                                               port=self.port,
                                               database=self.database)
        except mysql.connector.Error as exception:
            logging.error("database connectivity error: %s", str(exception))
            raise RuntimeError('database connectivity error') from exception

    @property
    def connector(self):
        return self.connector

    def query_full_table(self, table) -> List[Dict]:
        with self.cnx.cursor() as cursor:
            try:
                cursor.execute(f"SELECT * FROM {table};")
            except mysql.connector.Error as exception:
                logging.error("database operation error: %s", str(exception))
                raise RuntimeError('database operation error') from exception

            return [
                {col: val for col, val in zip(cursor.column_names, row)}
                for row in cursor.fetchall()
            ]
