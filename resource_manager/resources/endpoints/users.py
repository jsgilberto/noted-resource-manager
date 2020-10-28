""" Endpoints for user service
"""

USERS_SERVICE_ENDPOINT = {
    # user service endpoints
    'users_create': '/api/v1/users/',
    'users_get': '/api/v1/users/{user_id}/',
    'users_edit': '/api/v1/users/{user_id}/',

    # user service auth endpoints
    'retrieve_token': '/api/token/',
    'refresh_token': '/api/token/refresh/',
}
