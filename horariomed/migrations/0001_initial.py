# Generated by Django 3.2.5 on 2021-07-08 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horariomed',
            fields=[
                ('codigodehorario', models.IntegerField(max_length=7, primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('cedulamed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.medico')),
            ],
        ),
    ]