# Generated by Django 4.2.5 on 2023-09-30 04:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
