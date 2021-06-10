# Generated by Django 3.1.4 on 2021-06-10 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=200)),
                ('task_description', models.CharField(blank=True, max_length=200, null=True)),
                ('task_pic', models.ImageField(upload_to='')),
                ('create_time_stamp', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp2.user')),
            ],
        ),
    ]
