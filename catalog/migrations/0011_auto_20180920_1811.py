# Generated by Django 2.0 on 2018-09-20 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20180920_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
