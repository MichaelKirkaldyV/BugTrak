# Generated by Django 2.2.7 on 2020-01-14 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bugz', '0004_auto_20200106_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]