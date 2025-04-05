# Generated by Django 5.1.7 on 2025-03-31 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentID', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('paymentMethod', models.CharField(max_length=50)),
                ('paymentDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoiceID', models.AutoField(primary_key=True, serialize=False)),
                ('totalAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paymentStatus', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=20)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='bookings.booking')),
            ],
        ),
    ]
