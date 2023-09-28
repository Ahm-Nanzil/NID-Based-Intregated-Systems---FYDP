from django.db import models

# Create your models here.
# Create your models here.
class userfuck(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50 )
    user_mail= models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField( max_length=32 )