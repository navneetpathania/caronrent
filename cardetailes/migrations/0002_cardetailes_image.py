# Generated by Django 2.2.1 on 2019-06-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardetailes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardetailes',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]