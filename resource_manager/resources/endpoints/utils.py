from rest_framework.response import Response
from resource_manager.resources.endpoints.users import USERS_SERVICE_ENDPOINT
from resource_manager.resources.endpoints.documents import DOCUMENTS_SERVICE_ENDPOINT
import requests
import json
import os


class Service:
    """ Request transactions
    """
    USERS = 'users'
    DOCUMENTS = 'documents'

    def __init__(self, service, endpoint):
        """ Instance init
        """
        assert service == 'users' or service == 'documents'

        self._service = service
        if service == 'users':
            self._endpoint = USERS_SERVICE_ENDPOINT[endpoint]
        elif service == 'documents':
            self._endpoint = DOCUMENTS_SERVICE_ENDPOINT[endpoint]
    

    def _create_url(self, path_params=None):
        """ Creates url by service
        """
        # select a service
        if self._service == 'users':
            url = os.getenv('USERS_SERVICE_URL')
        elif self._service == 'documents':
            url = os.getenv('DOCUMENTS_SERVICE_URL')

        # add path parameters into string
        if path_params is not None:
            return url + self._endpoint.format(**path_params)
        return url + self._endpoint


    def make_request(self, request, path_params=None):
        """ This method makes the request to the selected service
        """
        url = self._create_url(path_params)
        headers = request.headers
        method = request.method

        if method == 'GET':
            try:
                response = requests.get(url, headers=headers)
                response = Response(response.json(), status=response.status_code)
            except:
                response = Response({"error": "Internal server error"}, status=500)
            return response

        elif method == 'POST':
            body = json.loads(request.body)
            try:
                response = requests.post(url, headers=headers, json=body)
                response = Response(response.json(), status=response.status_code)
            except:
                response = Response({"error": "Internal server error"}, status=500)
            return response

        elif method == 'PUT':
            body = json.loads(request.body)
            try:
                response = requests.put(url, headers=headers, json=body)
                response = Response(response.json(), status=response.status_code)
            except:
                response = Response({"error": "Internal server error"}, status=500)
            return response

        elif method == 'PATCH':
            body = json.loads(request.body)
            try:
                response = requests.patch(url, headers=headers, json=body)
                response = Response(response.json(), status=response.status_code)
            except:
                response = Response({"error": "Internal server error"}, status=500)
            return response
        
        elif method == 'DELETE':
            try:
                response = requests.delete(url, headers=headers)
                response = Response(response.json(), status=response.status_code)
            except:
                response = Response({"error": "Internal server error"}, status=500)
            return response