# Generated by Django 3.1.7 on 2021-06-11 01:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_auto_20210512_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
