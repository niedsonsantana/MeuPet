# Generated by Django 3.1.3 on 2020-11-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_animal_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='email',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='telefone',
            field=models.CharField(default='0', max_length=25),
            preserve_default=False,
        ),
    ]
