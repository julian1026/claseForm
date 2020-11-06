# Generated by Django 3.1.1 on 2020-10-02 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firs_name', models.CharField(max_length=50, verbose_name='nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='apellidos')),
                ('job', models.CharField(choices=[('4', 'OTRO'), ('1', 'INGENIERO'), ('0', 'CONTADOR'), ('2', 'ECONOMISTA'), ('3', 'ADMINISTRADOR')], max_length=1, verbose_name='trabajo')),
                ('Departamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamentos')),
            ],
        ),
    ]
