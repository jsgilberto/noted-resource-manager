# noted-resource-manager

[![Build Status](https://travis-ci.org/jsgilberto/noted-resource-manager.svg?branch=master)](https://travis-ci.org/jsgilberto/noted-resource-manager)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A resource manager for the noted app. Check out the project's [documentation](http://jsgilberto.github.io/noted-resource-manager/).

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
