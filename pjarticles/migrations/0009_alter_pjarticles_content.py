# Generated by Django 4.0.1 on 2022-01-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjarticles', '0008_pjarticles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pjarticles',
            name='content',
            field=models.TextField(verbose_name='Treść'),
        ),
    ]
