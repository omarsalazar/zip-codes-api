# zip-codes-api

[![Build Status](https://travis-ci.org/omarsalazar/zip-codes-api.svg?branch=master)](https://travis-ci.org/omarsalazar/zip-codes-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

API for zip codes. Make sure to check out the project's documentation on your [local environment](0.0.0.0:8001) or the
 [online documentation]() and the [API documentation (postman collection)](https://documenter.getpostman.com/view/3749457/2s9YRGw8h7)

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

- [Clone the repository](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository)


- Get in the root folder of the project
    ```commandline
    cd zip-codes-api
    ```

- Run in a terminal:
     ```
    cp .env.sample .env
    ```
 - Fill the environment variables in the new `.env` file
     ```properties
    DJANGO_SECRET_KEY=lkjrtjwpo489rupqweiofjcpweijf
    DJANGO_PAGINATION_LIMIT=20
    POSTGRES_DB=doorvel
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=secret
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    POSTGRES_CONN_MAX_AGE=60
    DJANGO_DEBUG=yes
    DJANGO_SETTINGS_MODULE=api.config
    ```

Start the dev server for local development:
```bash
docker-compose up
```
Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```



Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
