from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=100, blank=True)
    lang = models.CharField(max_length=100, blank=True)
    percentage = models.IntegerField()

    def __str__(self):
        if(self.skill and self.lang):
            return self.skill+','+self.lang
        if(self.lang):
            return self.lang
        if(self.skill):
            return self.skill
