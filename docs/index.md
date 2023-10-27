# zip-codes-api

[![Build Status](https://travis-ci.org/omarsalazar/zip-codes-api.svg?branch=master)](https://travis-ci.org/omarsalazar/zip-codes-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

API for zip codes. Check out the project's [documentation](http://omarsalazar.github.io/zip-codes-api/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

Once there's a superuser you can use [authentication](api/authentication.md) to make requests 
and create the elements needed to achieve the response given in the `exercise description`. Alternatively
you can use the `django administrator` tool to create the elements.

To use the `django administrator` tool you need to enter http://0.0.0.0:8000/admin/login/ once the 
project is initialized and access with the credentials previously entered when creating the superuser.

You can create each individual element or access the `ZipCode` section and create/search everything on the go.


![image1.png](api%2Fimage1.png)

There's also an option to import the information from the `data source` given in the 
`exercise description` (only for local development). You just need to download the information in Excel format

![image2.png](api%2Fimage2.png)

Enter http://0.0.0.0:8000/zip-codes/bulk/

![image3.png](api%2Fimage3.png)

Select the downloaded file and wait for the message indicating that 
everything went good c:

![image4.png](api%2Fimage4.png)


Now you can use the [zip code api](api/zip_codes.md) to check the response!  