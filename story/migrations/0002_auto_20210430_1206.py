# Generated by Django 3.1.7 on 2021-04-30 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='date_post',
            new_name='date_posted',
        ),
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
