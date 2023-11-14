from django.db import models
from django.contrib.auth.models import User

class Guide(models.Model):
    guideFname=models.CharField(max_length=30)
    guideLname=models.CharField(max_length=30)
    guideQualification=models.CharField(max_length=30)
    guideLanguage=models.CharField(max_length=50)
    guidePhone=models.CharField(max_length=15)
    guidePic=models.ImageField(upload_to="images/")
    guideEmail=models.CharField(max_length=30)
    guidePassword=models.CharField(max_length=15)
    registeredDate=models.DateTimeField(auto_now_add=True)
    forQuestion=models.TextField()
    forAnswer=models.TextField()

class Package(models.Model):
    packageName=models.CharField(max_length=100)
    packageFeature=models.CharField(max_length=200)
    packageLocation=models.CharField(max_length=100)
    packagePrice=models.CharField(max_length=10)
    packageImage=models.ImageField(upload_to='images/')
    packageDescription=models.TextField()
    createdDate=models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Guide, on_delete=models.CASCADE)

