# Generated by Django 2.2.2 on 2019-06-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default_image.jpg', upload_to=''),
        ),
    ]
