from rest_framework.decorators import api_view
from rest_framework.response import Response
from resource_manager.resources.endpoints.utils import (
    Service
)

"""
    User management:
"""

@api_view(['POST'])
def users_create(request):
    """ Resource for creating users
    """
    s = Service('users', 'users_create')
    response = s.make_request(request)
    return response


@api_view(['GET'])
def users_get(request, id):
    """ Resource for getting user info
    """
    s = Service('users', 'users_get')
    response = s.make_request(request, path_params={'user_id': id})
    return response


@api_view(['PUT', 'PATCH'])
def users_edit(request, id):
    """ Resource for editing a user
    """
    s = Service('users', 'users_edit')
    response = s.make_request(request, path_params={'user_id': id})
    return response



""" 
    User authentication:
"""

@api_view(['POST'])
def retrieve_token(request):
    """ Resource for issuing a token for a registered user
    """
    s = Service('users', 'retrieve_token')
    response = s.make_request(request)
    return response


@api_view(['POST'])
def refresh_token(request):
    """ Resource for refreshing a token
    """
    s = Service('users', 'refresh_token')
    response = s.make_request(request)
    return response

