from django.shortcuts import render
from .models import User,Client,Driver,DriverService,DriverStatus,UserService,ClientService
from .serializer import UserSerializer,ClientSerializer,DriverSerializer,DriverServiceSerializer,DriverStatusSerializer,UserServiceSerializer,ClientServiceSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly

#### USER ############

class ListCreateUserView(generics.ListCreateAPIView):
    #to handle get and post
    queryset  = User.objects.all() # Select * from user
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    #get user_id, put,patch
    queryset  = User.objects.all() # Select * from user
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

#### Client ##########

class ListCreateClientView(generics.ListCreateAPIView):
    #to handle get and post
    queryset  = Client.objects.all() # Select * from client
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    #get cleint_id, put,patch
    queryset  = Client.objects.all() # Select * from client
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    
### Driver############

class ListCreateDriverView(generics.ListCreateAPIView):
    #to handle get and post
    queryset  = Driver.objects.all() # Select * from driver
    serializer_class = DriverSerializer
    permission_classes = (IsAuthenticated,)

class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    #get user_id, put,patch
    queryset  = Driver.objects.all() # Select * from driver
    serializer_class = DriverSerializer
    permission_classes = (IsAuthenticated,)




# Create your views here.
