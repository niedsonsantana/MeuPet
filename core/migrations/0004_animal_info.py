# Generated by Django 3.1.3 on 2020-11-22 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201122_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='info',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]