# Generated by Django 4.1.5 on 2023-07-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_appp', '0012_rename_username_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='profile_image',
            field=models.ImageField(upload_to='media/profile_images/'),
        ),
    ]
