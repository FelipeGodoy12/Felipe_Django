# Generated by Django 4.0.3 on 2022-05-11 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Miaplicacion', '0004_categoria_alter_provedore_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_direccion', models.CharField(max_length=50)),
                ('calle_direccion', models.CharField(max_length=50)),
                ('ciudad_direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='provedore',
            name='direccion',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Miaplicacion.direccion'),
        ),
    ]