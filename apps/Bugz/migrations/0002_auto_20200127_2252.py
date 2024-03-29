# Generated by Django 2.2.7 on 2020-01-28 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bugz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigned_to',
            field=models.ForeignKey(max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bugz.User'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bugz.Project'),
        ),
    ]
