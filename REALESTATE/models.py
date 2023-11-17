from django.db import models
from django.contrib.auth.models import User


#create your models here

class Realtor(models.Model):
    TYPE = (
        ("Owner","Owner"),
        ("Agent","Agent"),
    )
   
    user = models.OneToOneField(User,null = True, on_delete = models.CASCADE, )
    First_name = models.CharField(max_length = 200,null = True)
    Last_name = models.CharField(max_length = 200,null = True)
    profile_pic = models.ImageField(upload_to = "Images",default ="Images/lee.jpg", blank = True,null = True,)
    facebook_link = models.URLField(max_length = 200,null = True,blank = True)
    instagram_link = models.URLField(max_length = 200,null = True,blank = True)
    
    description = models.TextField(max_length = 250,null = True, blank = True)
    email = models.EmailField(max_length = 200,null = True)
    phone_no = models.CharField(max_length = 200,null = True)
    WhatsApp_no = models.CharField(max_length = 200,null = True,blank = True)
    type = models.CharField(max_length = 200,null = True, choices = TYPE)
    date_created = models.DateTimeField(auto_now_add = True)
    
    
    
    class Meta:
        verbose_name_plural = "realtors"
        
    
    def __str__(self):
        return f" {self.user.realtor.First_name}  {self.user.realtor.Last_name}"
    
    
    
class tag(models.Model):
    CATEGORY = (
        ("House","House"),
        ("Apartment","Apartment"),
        ("Shop","Shop"),
        ("Office","Office"),
        ("Warehouse","Warehouse"),
        ("Land","Land"),
    )
    tag = models.CharField(max_length = 200,null = True, choices = CATEGORY)
    
    class Meta:
        verbose_name_plural = "tags"
    
    
    def __str__(self):
        return self.tag or ''
    
    
    
class Property(models.Model):
    
    LISTING = (
        ("Rent","Rent"),
        ("Sale","Sale"),
        ("Morgage","Morgage"),
    )
    realtor = models.ForeignKey(Realtor,on_delete = models.CASCADE,related_name='properties')
    tag = models.ForeignKey(tag,on_delete = models.CASCADE,null = True)
    Security = models.BooleanField(default=False)
    Parking = models.BooleanField(default=False)
    Internet = models.BooleanField(default=False)
    Playground = models.BooleanField(default=False)
    Furnished = models.BooleanField(default=False)
    Near_Shopping_Mall = models.BooleanField(default=False)
    Balcony = models.BooleanField(default=False)
    Backup_water_supply = models.BooleanField(default=False)
    Backup_electricity_supply = models.BooleanField(default=False)
    title = models.CharField(max_length = 200,null = True)
    no_of_bedroom = models.IntegerField(null = True)
    no_of_bathroom = models.IntegerField(null = True)
    size_of_land = models.CharField(max_length = 100,null = True, blank = True)
    size_of_space = models.CharField(max_length = 100,null = True, blank = True)
    description = models.TextField(max_length = 250,null = True, blank = True)
    location = models.CharField(max_length = 200,null = True)
    ward = models.CharField(max_length = 200,null = True)
    town = models.CharField(max_length = 200,null = True)
    list = models.CharField(max_length = 200,null = True, choices = LISTING)
    price = models.DecimalField(max_digits = 9,decimal_places = 2 ,null = True)
    main_photo = models.ImageField(upload_to = 'Images')
    photo_1 = models.ImageField(upload_to = 'Images')
    photo_2 = models.ImageField(upload_to = 'Images')
    photo_3 = models.ImageField(upload_to = 'Images')
    photo_4 = models.ImageField(upload_to = 'Images')
    photo_5 = models.ImageField(upload_to = 'Images')
    availability = models.BooleanField(default = True)
    date_of_listing = models.DateTimeField(auto_now_add= True)
   
    
    class Meta:        
        verbose_name_plural = "Properties"
        ordering = ['-date_of_listing']
        indexes = [
        models.Index(fields=['-date_of_listing']),
        ]
        
    
    def __str__(self):
        return f" {self.title} in {self.location}"
    


        

class customer (models.Model):
    name = models.CharField(max_length = 200,null = True)
    email = models.EmailField(max_length = 200,null = True)
    phone_no = models.CharField(max_length = 200,null = True)
    date_created = models.DateTimeField(auto_now_add = True)
    
    
    
    class Meta:
        verbose_name_plural = "customers"
    
    def __str__(self):
        return self.name
    
    

    
