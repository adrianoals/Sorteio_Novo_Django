# Generated by Django 5.0.1 on 2024-01-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio_novo', '0008_delete_vagaescolher'),
    ]

    operations = [
        migrations.AddField(
            model_name='listadepresenca',
            name='vaga',
            field=models.CharField(choices=[('vaga1', 'Vaga 1'), ('vaga2', 'Vaga 2')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='listadepresenca',
            name='apartamento',
            field=models.CharField(choices=[('apartamento1', 'Apartamento 1'), ('apartamento2', 'Apartamento 2')], max_length=100),
        ),
    ]
