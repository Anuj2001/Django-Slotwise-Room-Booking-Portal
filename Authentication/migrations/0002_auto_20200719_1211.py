# Generated by Django 3.0.7 on 2020-07-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user_model',
            name='contact_no',
            field=models.IntegerField(default=0),
        ),
    ]
