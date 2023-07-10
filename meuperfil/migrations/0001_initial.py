# Generated by Django 4.1.7 on 2023-02-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('bloco', models.CharField(default='SB', max_length=2)),
                ('unidade', models.CharField(default='SU', max_length=5)),
                ('observacoes', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]