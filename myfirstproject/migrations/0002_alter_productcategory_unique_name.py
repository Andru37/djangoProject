# Generated by Django 4.0.6 on 2022-08-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='unique_name',
            field=models.SlugField(null=True),
        ),
    ]
