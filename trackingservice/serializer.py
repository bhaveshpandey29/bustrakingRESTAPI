from rest_framework import serializers
from .models import User,Client,Driver,DriverService,DriverStatus,UserService,ClientService

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User
    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Client

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Driver

class DriverServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DriverService

class DriverStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = DriverStatus

class UserServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UserService

class ClientServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ClientService