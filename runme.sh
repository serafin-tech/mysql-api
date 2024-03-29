#!/bin/bash

if [[ ! -d venv ]]
then
  python3.11 -m venv venv
fi

source venv/bin/activate
python3.11 -m pip install -U pip
python3.11 -m pip install -r requirements.txt

echo "Test command: curl -i http://localhost:8000/"

uvicorn mysql_api.api:app --reload
