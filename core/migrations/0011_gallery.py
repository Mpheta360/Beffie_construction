# Generated by Django 4.2.5 on 2023-11-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_allproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
