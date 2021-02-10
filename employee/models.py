from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee" 

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    class Meta:
        db_table = "Category"

class Test(models.Model):
    test = models.CharField(max_length=200)
    class Meta:
        db_table = "Test"

class Dash_Cateogry(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    category_level = models.IntegerField()
    business_profile_id = models.IntegerField()
    class Meta:
        db_table = "dash_category"