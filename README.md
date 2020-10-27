# noted-resource-manager

[![Build Status](https://travis-ci.org/jsgilberto/noted-resource-manager.svg?branch=master)](https://travis-ci.org/jsgilberto/noted-resource-manager)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

A resource manager for the noted app. Check out the project's [documentation](http://jsgilberto.github.io/noted-resource-manager/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```


This resource manager is used to normalize the API calls from the front end. For example, if one of the APIs version change, we only have to change
logic inside the resource manager and never on the front end.

It also serves as the entrypoint for all the remaining resources, being the only service exposed to the public.
