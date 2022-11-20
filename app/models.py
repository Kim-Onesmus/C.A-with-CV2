from django.db import models

# Create your models here.

class student(models.Model):
    admission = models.CharField (max_length=10)
    upload = models.CharField(max_length=10)
    
    def __str__(self):
        return self.admission
    
        