# Generated by Django 5.0.1 on 2024-01-25 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorteio_novo', '0007_rename_presenca_vagaescolher_lista_de_presenca'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VagaEscolher',
        ),
    ]
