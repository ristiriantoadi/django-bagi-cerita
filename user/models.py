from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=30, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)

    # gender field configurations
    Laki = 'L'
    Perempuan = 'P'
    GENDER_CHOICES = [
        (Laki, 'Laki-laki'),
        (Perempuan, 'Perempuan'),
    ]
    gender = models.CharField(max_length=30,blank=True, choices=GENDER_CHOICES)

    kota = models.CharField(max_length=30, blank=True)
    tentang_saya = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'