from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

"""
    User management:
"""

@api_view(['POST'])
def users_create(request):
    """ Resource for creating users
    """
    return Response({})


@api_view(['GET'])
def users_get(request, id):
    """ Resource for getting user info
    """
    return Response({})


@api_view(['PUT', 'PATCH'])
def users_edit(request, id):
    """ Resource for editing a user
    """
    return Response({})



""" 
    User authentication:
"""

@api_view(['POST'])
def retrieve_token(request):
    """ Resource for issuing a token for a registered user
    """
    return Response({})


@api_view(['POST'])
def refresh_token(request):
    """ Resource for refreshing a token
    """
    return Response({})


# @api_view(["POST"])
# def verify_token(request):
#     """ Resource used to verify a given token
#     """
#     return Response({})