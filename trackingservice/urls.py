from django.urls import path
from .views import ListCreateClientView,ClientDetailView,UserDetailView,ListCreateUserView

urlpatterns = [
    path('user/',ListCreateUserView.as_view(),name = "list-create-user"),
    path('user/<uuid:pk>',UserDetailView.as_view(),name = "update-delete-user"),
    path('client/',ListCreateClientView.as_view(),name = "list-create-client"),
    path('client/<uuid:pk>',ClientDetailView.as_view(),name = "update-delete-client")
]