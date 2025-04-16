from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    date_d_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
