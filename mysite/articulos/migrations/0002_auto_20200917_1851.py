# Generated by Django 2.2.7 on 2020-09-17 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='etiquetaP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='etiquetaP',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='articulos.etiquetaP', verbose_name='Etiqueta Principal'),
        ),
    ]
