from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    programme = models.CharField(max_length=500)
    email = models.EmailField()
    nationality = models.CharField(max_length=500)
    age = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    
    def __str__(self):
        return self.firstname