from django.db import models

# Create your models here.
class User(models.Model):
    whatsapp_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    business_type = models.CharField(max_length=100, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
