# Generated by Django 5.1.7 on 2025-03-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0004_alter_admin_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='permissions',
        ),
        migrations.AddField(
            model_name='admin',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.permission'),
        ),
    ]
