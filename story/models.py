from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=120,blank=True)
    date_posted = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'{self.title} Cerita'

    class Meta:
        ordering = ["-date_posted"]