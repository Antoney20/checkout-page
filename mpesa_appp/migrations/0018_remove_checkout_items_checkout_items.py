# Generated by Django 4.1.5 on 2023-07-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_appp', '0017_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='items',
        ),
        migrations.AddField(
            model_name='checkout',
            name='items',
            field=models.ManyToManyField(to='mpesa_appp.item'),
        ),
    ]