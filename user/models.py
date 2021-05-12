from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=30, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    kota = models.CharField(max_length=30, blank=True)
    tentang_saya = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture',blank=True)
    points = models.IntegerField(default=20)

    # gender field configurations
    Laki = 'L'
    Perempuan = 'P'
    GENDER_CHOICES = [
        (Laki, 'Laki-laki'),
        (Perempuan, 'Perempuan'),
    ]
    gender = models.CharField(max_length=30,blank=True, choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.user.username} Profile'