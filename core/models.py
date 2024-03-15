from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
# Create your models here.

class CustomUser(models.Model):
    
    id = models.AutoField(primary_key = True)    
    name = models.CharField(max_length = 200)
    card_no = models.CharField(max_length=30)
    phone_number = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^(?:\+20|0)?1\d{9}$')],
        help_text="Enter a valid phone number. Up to 11 digits allowed.",
        null = True
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # this function to hash password 
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(CustomUser,self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True,blank=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)    

    def __str__(self):
        return self.name 
    
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    website = models.URLField()
    image = models.ImageField(upload_to='images',blank=True,null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    code = models.CharField(max_length=255)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Branches(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    