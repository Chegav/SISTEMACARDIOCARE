# Generated by Django 3.2.5 on 2021-07-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citamed', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citamedica',
            old_name='cedula',
            new_name='cedulapac',
        ),
        migrations.AlterField(
            model_name='citamedica',
            name='codigocitamed',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
