from django.db import models

from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade = models.IntegerField()
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"# Create your models here.
