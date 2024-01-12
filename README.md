# mysql-api

REST API to read data from MySQL

## Setup instructions

### Linux

```shell
python3.11 -m venv venv
source venv/bin/activate
python3.11 -m pip install -U pip
python3.11 -m pip install -r requirements.txt
```

### Windows
...

## Configuration

```dotenv
MYSQL_HOST="<hostname, default 127.0.0.1>"
MYSQL_PORT="<port_number, default 3306>"
MYSQL_USER="<user_name>"
MYSQL_PASS="<password>"
MYSQL_DATABASE="<schema_name>"

DEBUG="<True | False>"
```

## Testing / using

```shell
curl http://127.0.0.1:8000/status
curl -s http://127.0.0.1:8000/table/<table_name> | jq
```
