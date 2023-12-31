# Generated by Django 4.2.5 on 2023-12-05 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('pdescription', models.TextField(max_length=1000)),
                ('pprice', models.FloatField()),
                ('p_image', models.ImageField(upload_to='products')),
            ],
        ),
    ]
