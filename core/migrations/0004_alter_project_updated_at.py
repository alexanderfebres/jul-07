# Generated by Django 4.0.6 on 2022-07-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_project_created_at_alter_project_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
