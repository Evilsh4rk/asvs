# Generated by Django 2.0.6 on 2018-06-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='project_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
