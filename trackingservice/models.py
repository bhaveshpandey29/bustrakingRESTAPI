from django.db import models
import uuid
import random as r

class User(models.Model):
    user_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    name = models.CharField(max_length = 30)
    contact_no = models.CharField(max_length = 10)
    user_name = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 30)
    email_address = models.EmailField(unique = True) # CheckOnce
    token_no = models.IntegerField(default=r.randrange(1000,10000))
    profile_pic = models.ImageField(upload_to = "user/profile/pic")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Client(models.Model):
    client_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    name = models.CharField(max_length = 30)
    user_name = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 30)
    email_address = models.EmailField(unique = True) # CheckOnce
    token_no = models.IntegerField(default=r.randrange(1000,10000))
    profile_pic = models.ImageField(upload_to = "user/profile/pic")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Driver(models.Model):
    driver_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    name = models.CharField(max_length = 30)
    contact_no = models.CharField(max_length = 10, unique = True)
    address = models.TextField()
    token_no = models.IntegerField(default=r.randrange(1000,10000))
    profile_pic = models.ImageField(upload_to = "user/profile/pic")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# Services

class DriverService(models.Model):
    service_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    driver = models.ForeignKey(Driver,on_delete= models.CASCADE)
    start_lat = models.FloatField()
    start_long = models.FloatField()
    stop_lat = models.FloatField(null = True,blank=True)
    stop_long = models.FloatField(null = True,blank=True)
    bus_no = models.CharField(max_length = 15)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.service_id)

class DriverStatus(models.Model):
    status_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    lat = models.FloatField()
    lng = models.FloatField()
    driver_service = models.ForeignKey(DriverService,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.status_id)

class UserService(models.Model):
    service_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.service_id)

class ClientService(models.Model):
    service_id = models.UUIDField(default = uuid.uuid4,primary_key = True,editable = False)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    driver = models.ForeignKey(Driver,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.service_id)
