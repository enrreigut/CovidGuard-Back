# Generated by Django 3.1.4 on 2021-05-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadisticasTipo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('lugar_de_residencia', models.CharField(blank=True, max_length=150, null=True)),
                ('total_confirmados', models.IntegerField(blank=True, null=True)),
                ('tasa_total_confirmados', models.FloatField(blank=True, null=True)),
                ('confirmados_PDIA', models.IntegerField(blank=True, null=True)),
                ('tasa_PDIA', models.FloatField(blank=True, null=True)),
                ('confirmados_PDIA_14', models.IntegerField(blank=True, null=True)),
                ('tasa_PDIA_14', models.FloatField(blank=True, null=True)),
                ('confirmados_PDIA_7', models.IntegerField(blank=True, null=True)),
                ('tasa_PDIA_7', models.FloatField(blank=True, null=True)),
                ('curados', models.IntegerField(blank=True, null=True)),
                ('fallecidos', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
