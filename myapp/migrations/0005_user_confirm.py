# Generated by Django 4.0 on 2022-10-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_bloodgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm',
            field=models.CharField(default='', max_length=20),
        ),
    ]
