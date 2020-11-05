from django.urls import path
from resource_manager.resources.documents import views


urlpatterns = [
    path('documents/', views.list_or_create_document),
    path('documents/<str:slug>/', views.get_update_delete_document),
]
