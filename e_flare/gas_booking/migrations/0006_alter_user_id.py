# Generated by Django 5.0 on 2024-01-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_booking', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
