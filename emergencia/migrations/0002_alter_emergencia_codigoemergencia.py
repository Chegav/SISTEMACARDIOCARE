# Generated by Django 3.2.5 on 2021-07-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergencia',
            name='codigoemergencia',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
