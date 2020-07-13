from django.db import models

# Create your models here.
class Education(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.title
