# Generated by Django 4.0 on 2022-10-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_user_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
