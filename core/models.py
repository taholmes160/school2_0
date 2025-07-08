from django.db import models
from django.contrib.auth.models import User  # Using default User for staff for now



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

class StudentNote(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # user who wrote the note
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return f"Note by {self.author} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"