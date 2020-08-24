#!/bin/bash

## Configuring environment
pip install -r requires.txt

## Static verification
#pylint *.py
bandit *.py --skip B101

## Testing
pytest --verbose src/test_db.py
pytest --verbose src/test_orm.py

## Creating setup
scripts/create-self-cert.sh
docker-compose down --volumes
docker-compose up --build -d

## System tests
./tests/wait_for_url.sh 60 https://localhost:8050 && \
pytest tests/test_system.py
