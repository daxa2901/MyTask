from django.db import  models
from django.db.models.fields import CharField

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    join_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    password = models.CharField(max_length=300)
    def __str__(self) :
        return self.username


class Task(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey("User", on_delete=models.CASCADE, related_name='userid')
    task_title = models.CharField(max_length=200)
    task_description =models.CharField(max_length=2000,null=True, blank=True)
    task_pic = models.URLField(max_length=200,null=True,blank=True)
    create_time_stamp= models.DateTimeField(auto_now_add=False)