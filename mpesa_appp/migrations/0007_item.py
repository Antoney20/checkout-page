# Generated by Django 4.1.5 on 2023-07-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_appp', '0006_alter_registration_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item_image', models.ImageField(upload_to='item/images')),
            ],
        ),
    ]
