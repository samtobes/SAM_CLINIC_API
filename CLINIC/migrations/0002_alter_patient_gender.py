# Generated by Django 4.2.6 on 2023-10-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLINIC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
