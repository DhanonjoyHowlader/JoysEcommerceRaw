# Generated by Django 3.1.2 on 2020-11-14 10:54

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=50)),
                ('Mobile_number', models.CharField(max_length=30)),
                ('Profile_Picture', models.ImageField(blank=True, null=True, upload_to='users/profile_pictures')),
                ('Email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_of_Birth', models.DateField()),
                ('Gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (3, 'Other')])),
                ('Billing_address', models.TextField(max_length=500)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]