# Generated by Django 3.1.2 on 2020-11-14 18:44

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
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(1, 'In Stock'), (2, 'Out of Stock')])),
                ('image', models.ImageField(blank=True, default='products/images/default.jpg', upload_to='products/images/')),
                ('file', models.FileField(blank=True, default='products/files/default.pdf', null=True, upload_to='products/files/')),
                ('reviews', models.ManyToManyField(to='ProductManagement.Review')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Delivering', 'Delivering'), ('Completed', 'Completed')], default='Pending', max_length=30)),
                ('payment_options', models.CharField(choices=[('Bkash', 'Bkash'), ('Rocket', 'Rocket'), ('Payment on delivery', 'Payment on delivery')], default='Payment on delivery', max_length=50)),
                ('is_paid', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(blank=True, max_length=30, null=True)),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ProductManagement.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ManyToManyField(to='ProductManagement.Product')),
            ],
        ),
    ]