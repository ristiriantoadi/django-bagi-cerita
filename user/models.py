from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # middle_name = models.CharField(max_length=30, blank=True)
    # dob = models.DateField(null=True, blank=True)
    nama_lengkap = models.CharField(max_length=30, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'