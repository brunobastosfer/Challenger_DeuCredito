# Generated by Django 3.2.8 on 2021-10-11 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0002_alter_cars_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='model',
            field=models.CharField(choices=[('1', 'hatch'), ('2', 'Sedan'), ('3', 'SUV')], default='1', max_length=1),
        ),
    ]
