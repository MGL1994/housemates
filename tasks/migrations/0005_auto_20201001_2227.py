# Generated by Django 3.1.1 on 2020-10-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200920_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(default='', null=True, related_name='tasks', to='tasks.Tag'),
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
