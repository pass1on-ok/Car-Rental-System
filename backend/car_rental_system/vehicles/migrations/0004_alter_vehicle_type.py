# Generated by Django 5.1.7 on 2025-04-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_alter_car_fueltype_alter_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Two-Door Sedan', 'Two-Door Sedan'), ('Hatchback', 'Hatchback (Liftback)'), ('Coupe', 'Coupe'), ('Limousine', 'Limousine'), ('Minivan', 'Minivan'), ('Hardtop', 'Hardtop'), ('Town Car', 'Town Car'), ('Kombi', 'Kombi'), ('Fastback', 'Fastback'), ('Crossover', 'Crossover'), ('Phaeton', 'Phaeton'), ('Lando', 'Lando'), ('Targa', 'Targa'), ('Roadster', 'Roadster (Convertible, Spyder, Speedster)'), ('Torpedo', 'Torpedo'), ('Barchetta', 'Barchetta')], default='Sedan', max_length=30),
        ),
    ]
