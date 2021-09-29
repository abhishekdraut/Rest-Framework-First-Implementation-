from django.db import models

# Create your models here.

class blog(models.Model):                                                                               
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255,null=True,blank=True)
    date=models.DateField(null=True,blank=True)

    def __str__(self):
        return (self.title)