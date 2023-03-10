# Generated by Django 4.1.1 on 2022-12-20 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('institucion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_inscripcion', models.DateField()),
                ('institucion', models.CharField(choices=[('Universidad Catolica de Temuco', 'Universidad Catolica de Temuco'), ('Universidad de Chile', 'Universidad de Chile'), ('Universidad de la frontera', 'Universidad de la frontera'), ('Universidad Santo Tomas', 'Universidad Santo Tomas'), ('Universidad Autonoma de Chile', 'Universidad Autonoma de Chile'), ('Inacap', 'Inacap'), ('AIEP', 'AIEP')], default='Universidad Catolica', max_length=50)),
                ('hora_inscripcion', models.TimeField()),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO ASISTEN', 'No Asisten')], default='RESERVADO', max_length=20)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
