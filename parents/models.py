from django.db import models

# Create your models here.
class Parents(models.Model):
    parent = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    student = models.ForeignKey('auth.User', on_delete=models.CASCADE)