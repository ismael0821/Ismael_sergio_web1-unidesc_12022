# Generated by Django 4.0.5 on 2022-06-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financeira', models.CharField(max_length=100)),
                ('nomeCliente', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('dataAbertura', models.DateField(max_length=100)),
            ],
        ),
    ]
