# Generated by Django 2.2.7 on 2019-12-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20191202_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
