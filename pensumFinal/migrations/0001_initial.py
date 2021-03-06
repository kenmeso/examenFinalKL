# Generated by Django 2.0.9 on 2018-11-19 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('seccion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Listado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensumFinal.Grado')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('grados', models.ManyToManyField(through='pensumFinal.Listado', to='pensumFinal.Grado')),
            ],
        ),
        migrations.AddField(
            model_name='listado',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensumFinal.Materia'),
        ),
    ]
