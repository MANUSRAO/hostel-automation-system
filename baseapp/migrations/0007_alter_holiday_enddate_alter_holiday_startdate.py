# Generated by Django 4.1.6 on 2023-02-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0006_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='endDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='startDate',
            field=models.DateTimeField(),
        ),
    ]
