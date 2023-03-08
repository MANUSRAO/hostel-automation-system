# Generated by Django 4.1.6 on 2023-02-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0011_alter_holiday_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('morn', models.IntegerField(default=5)),
                ('aft', models.IntegerField(default=5)),
                ('night', models.IntegerField(default=5)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
