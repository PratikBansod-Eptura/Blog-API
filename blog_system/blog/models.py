from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    gender_choice = (('male','Male'),
                     ('female', 'Female'))
    gender = models.CharField(max_length=32, choices=gender_choice)
    mob_number = models.BigIntegerField(null=True)
    city = models.CharField(max_length=32)


class Blog(models.Model):
    user = models.ForeignKey(CustomUser, related_name='blog', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    last_updated_on = models.DateField(auto_now=True)
    approval_status = models.BooleanField(default=False)

