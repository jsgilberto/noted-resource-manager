from django.urls import path

from resource_manager.resources.users import views

urlpatterns = [
    # User management
    path('users/', views.users_create),
    path('users/<str:id>/', views.users_get),
    path('users/<str:id>/', views.users_edit),

    # User authentication
    path('token/', views.retrieve_token),
    path('token/refresh/', views.refresh_token),
]