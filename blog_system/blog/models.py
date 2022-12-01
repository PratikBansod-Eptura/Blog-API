from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Blog(models.Model):
    user = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField()
    published_date = models.DateField()
    last_updated_on = models.DateField()
    approval_status = models.BooleanField(default=False)

class CustomUser(AbstractUser):
    gender_choice = (('Male','male'),
                     ('Female', 'female'))
    gender = models.CharField(max_length=32, choices=gender_choice)
    mob_number = models.BigIntegerField(null=True)
    city = models.CharField(max_length=32)