from django.db import models

# Create your models here.
class Blog(models.Model):
    user = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    description = models.TextField()
    published_date = models.DateField()
    last_updated_on = models.DateField()
    approval_status = models.BooleanField(default=False)
