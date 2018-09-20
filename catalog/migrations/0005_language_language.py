# Generated by Django 2.0 on 2018-09-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180917_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='language',
            field=models.CharField(choices=[('Eng', 'English'), ('Spa', 'Spanish'), ('Fre', 'French')], default='Eng', help_text='Language book instance is published', max_length=3),
        ),
    ]