# Generated by Django 3.0.2 on 2020-01-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200128_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso', models.CharField(max_length=50, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=150, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete'), ('lni-leaf', 'Folha'), ('lni-laptop-phone', 'Laptop'), ('lni-envelope', 'Envelope')], max_length=16, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=150, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='servico',
            field=models.CharField(max_length=50, verbose_name='Serviço'),
        ),
    ]
