from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length= 20)
    email=models.CharField(max_length=40,unique=True)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=100,default="customer")
   

class Booking(models.Model):
    customerName=models.CharField(max_length=30)
    contactNumber=models.IntegerField()
    deliveryAddress=models.CharField(max_length=60)
    cylinderType=models.CharField(max_length=30)
    quantity=models.IntegerField()


class Employees(models.Model):
    fullName=models.CharField(max_length=100) 
    empCode=models.CharField(max_length=10)
    mobileNumber=models.CharField(max_length=15)
    MANAGER ='manager'
    DELIVERY_STAFF ='delivery_staff'
    OFFICE_STAFF ='office_staff'
    POSITION_CHOICES =[
        (MANAGER,'Manager'),
        (DELIVERY_STAFF,'Delivery Staff'),
        (OFFICE_STAFF,'Office Staff')
    ]
    position=models.CharField(max_length=30,choices=POSITION_CHOICES,default=MANAGER)

class Profile(models.Model):
    name=models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    dob=models.DateField()
    marital_status=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    document=models.CharField(max_length=50)








