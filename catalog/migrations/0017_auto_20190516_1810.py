# Generated by Django 2.0 on 2019-05-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20181024_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birthdate (yyyy-mm-dd'),
        ),
    ]
