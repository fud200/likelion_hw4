# Generated by Django 2.2.2 on 2019-06-20 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField(blank=True, null=True)),
                ('room', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_from'],
            },
        ),
    ]
