# Generated by Django 3.1.3 on 2020-11-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201123_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='telefone',
            new_name='fone',
        ),
        migrations.AddField(
            model_name='animal',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
    ]
