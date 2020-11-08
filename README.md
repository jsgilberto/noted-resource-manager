# Noted: Resource manager

[![Build Status](https://travis-ci.org/jsgilberto/noted-resource-manager.svg?branch=master)](https://travis-ci.org/jsgilberto/noted-resource-manager)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

### About the project

This repo contains the service for the resource manager in Noted app.

This service is similar to what an API Gateway would do, it acts as the front door of the remaining services (users and documents). The intention here is that this service decides which services are available in the background and selects which endpoints from these services are available for the public. It means that there are public endpoints and private endpoints. Public endpoints are available to use from the resource manager service but on the other hand, private endpoints are only available to use from other internal services.

This resource manager is used to normalize the API calls from the front end. For example, if one of the APIs version change, we only have to change
logic inside the resource manager and never on the front end.

It also serves as the entrypoint for all the remaining resources, being the only service exposed to the public.

### How does it work

All requests for public endpoints are tunneled to the requested resource. For instance, if you would like to authenticate in the front end, you would have to use the users service, but the clients only have acces to the users service through the resource manager service.

<p align="center">
  <img src="images/noted-resource-manager.png" />
</p>

## Built with
This project was started with a cookiecutter template from gh:agconti/cookiecutter-django-rest which comes with a set of libraries for creating REST APIs with Python and Django:

- Python
- Django
- Django Rest Framework
- Postgres
- Docker
- Requests module
- And more

If you want to see the full list please go ahead and read the `requirements.txt` file where you can find all the used dependencies.

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

## Getting started

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Jesus Alvarez - in/alvarezjesus - alv.mtz94@gmail.com

Project link: https://github.com/jsgilberto/noted-users-service

## Acknowledgements

* [cookiecutter-django-rest](https://github.com/agconti/cookiecutter-django-rest)
