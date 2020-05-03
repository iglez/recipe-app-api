# recipe-app-api
Recipe app api source code.

# Docker commands
## Create app
`docker-compose run --rm app sh -c "python manage.py startapp recipe"`

## Test and lint
`docker-compose run --rm app sh -c "python manage.py test && flake8"`

## Make migrations
`docker-compose run --rm app sh -c "python manage.py makemigrations core"`

