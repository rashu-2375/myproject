from django.db import models
class service(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Address = models.TextField()

# Create your models here.
