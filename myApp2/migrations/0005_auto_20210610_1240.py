# Generated by Django 3.1.4 on 2021-06-10 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp2', '0004_auto_20210610_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
