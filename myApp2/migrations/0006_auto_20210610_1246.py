# Generated by Django 3.1.4 on 2021-06-10 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp2', '0005_auto_20210610_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to='myApp2.user'),
        ),
    ]
