# Generated by Django 4.0 on 2022-10-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_user_age_alter_user_bloodgroup_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
