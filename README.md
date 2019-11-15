[![Build Status](https://travis-ci.org/rso-projekt-leon/data-upload.svg?branch=master)](https://travis-ci.org/rso-projekt-leon/data-upload)

# data-upload
Data upload microservice.

## Development
### venv
Run app: 
- `export FLASK_APP=app/__init__.py`
- `export FLASK_ENV=development`
- `python manage.py run`

### Docker
Build image:
- `chmod +x entrypoint.sh` (first time)
- `docker-compose build`

Start container:
- `docker-compose up -d --build`

Stop container:
- `docker-compose down -v`

### Testing
- `docker-compose exec upload  pytest "app/tests" -p no:warnings"`

## Endpoints
### Info
Informacije o projektu:
- `/v1/demo/info`

Nalaganje dataseta:
- `/v1/upload/dataset`
