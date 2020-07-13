from django.db import models

# Create your models here.
class Interests(models.Model):
    Hobby=models.CharField(max_length=50)

    def __str__(self):
        return self.Hobby

