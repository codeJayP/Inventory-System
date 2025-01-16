from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField(max_length=50, unique=True)

class Equipment(models.Model):
    property_num = models.IntegerField(unique=True)
    article_item = models.CharField(max_length=50)
    description = models.TextField()
    person_accountable = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=100)
    date_save = models.DateTimeField(auto_now_add=True)
    make_changes = models.DateTimeField(auto_now=True)