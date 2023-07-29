from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.


class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, null=True)
    estb = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(null=True, blank=True)
    estb = models.DateField(null=True)
    contact = models.CharField(max_length=100, null=True)
    owner = models.CharField(max_length=100, null=True)

    showroom=models.ForeignKey(ShowRoom, on_delete=models.CASCADE, related_name='brands', null=True)
    
    def __str__(self) -> str:
        return self.name


class Model(models.Model):
    name =  models.CharField(max_length=100, unique=True)
    picture = models.ImageField(null=True, blank=True)
    generation =  models.IntegerField(null=True)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brands', null=True)

    def __str__(self) -> str:
        return self.name

class EngineModel(models.Model):
    engine =  models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100,null=True, choices= [('G','Gasoline'), ('D' ,'Diesel')] )
    manufacturer = models.CharField(max_length=100, null=True)
    year = models.DateField(null=True)

    def __str__(self) -> str:
        return self.engine

class Engine(models.Model):
    engineNo = models.CharField(max_length=100, primary_key=True)
    
    engineModel = models.ForeignKey(EngineModel,on_delete=models.CASCADE, related_name='engines',unique=True,)

    def __str__(self) -> str:
        return self.engineNo

class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='cars', null=True)
    year = models.IntegerField(null=True)
    ChasisNo = models.CharField(max_length=100, primary_key=True)
    engine = models.OneToOneField(Engine, on_delete=models.CASCADE, related_name='cars', null=True )
    
    def __str__(self) -> str:
        return self.ChasisNo


class Features(models.Model):
    model = models.OneToOneField(Model, on_delete=models.CASCADE, related_name='features', null=True)
    seating_Capacity = models.IntegerField(null=True)
    horsepower = models.IntegerField(null=True)
    topspeed = models.IntegerField(null=True)
    torque = models.IntegerField(null=True)
    transmission = models.CharField(null=True, max_length=1, choices= [('A', 'Automatic'), ('M', 'Manual')])
    abs_brakes = models.BooleanField(default=True)
    leather_seats = models.BooleanField(default=True)
    heated_seats = models.BooleanField(default=True)
    sunroof = models.BooleanField(default=True)
    turboCharger = models.BooleanField(default=True)


    

class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(null=True, max_length=1, choices= [('M', 'Male'), ('F', 'Female')])
    qualification = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    showroom = models.ForeignKey(ShowRoom, on_delete=models.CASCADE, related_name='staffs', null=True)

    def __str__(self) -> str:
        return self.name
