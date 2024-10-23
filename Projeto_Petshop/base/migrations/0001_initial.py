# Generated by Django 4.2.11 on 2024-07-06 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data Envio')),
                ('lido', models.BooleanField(blank=True, default=False, verbose_name='Lido')),
            ],
            options={
                'verbose_name': 'Formulário de Contato',
                'verbose_name_plural': 'Formulários de Contatos',
                'ordering': ['-data'],
            },
        ),
    ]