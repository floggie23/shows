from django.db import models

# Create your models here.

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    desc = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)