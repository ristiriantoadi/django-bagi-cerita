# Generated by Django 3.1.7 on 2021-05-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_tag_stories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date_posted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
