# Generated by Django 5.0 on 2024-01-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_booking', '0007_position_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='position',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
