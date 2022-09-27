# Generated by Django 4.0.4 on 2022-05-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_fname', models.CharField(max_length=30, verbose_name='First name')),
                ('customer_lname', models.CharField(max_length=30, verbose_name='Last name')),
                ('customer_db', models.DateField()),
                ('customer_gender', models.CharField(choices=[('man', 'man'), ('woman', 'woman')], max_length=10, verbose_name='gender')),
                ('customer_address', models.CharField(max_length=50, verbose_name='Address')),
                ('customer_email', models.CharField(max_length=40, unique=True, verbose_name='email')),
                ('customer_password', models.CharField(max_length=30, unique=True, verbose_name='email password')),
                ('customer_number', models.CharField(max_length=20, unique=True, verbose_name='Telephone_number')),
                ('customer_city', models.CharField(max_length=20, verbose_name='City')),
                ('customer_drive_license', models.ImageField(upload_to='img/Customer_License/')),
            ],
        ),
    ]
