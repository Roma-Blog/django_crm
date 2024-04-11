from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 100)
    birthday = models.DateField()
    phone = models.CharField(max_length = 15)
    email = models.EmailField(blank=True)

     
