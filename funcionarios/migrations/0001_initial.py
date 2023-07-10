# Generated by Django 4.1.7 on 2023-03-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=20)),
                ('genero', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], default='O', max_length=1)),
                ('tipo_usuario', models.CharField(choices=[('C', 'Condômino'), ('S', 'Síndico'), ('O', 'Outros')], default='O', max_length=1)),
                ('observacoes', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]