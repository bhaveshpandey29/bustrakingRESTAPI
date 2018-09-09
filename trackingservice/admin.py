from django.contrib import admin
from .models import User,Client,Driver,DriverService,DriverStatus,UserService,ClientService

admin.site.register([User,Client,Driver,DriverService,DriverStatus,UserService,ClientService])

# Register your models here.
