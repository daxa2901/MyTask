from django.db.models import fields
from rest_framework import serializers
from myApp2.models import User,Task

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid','username','join_date','password']

    def validate_username(self,value):
        if value[0].lower()!= 'a':
            raise serializers.ValidationError("usename must start with a or A")
        if len(value)<10:
            raise serializers.ValidationError("usename must me of 10 charecter")
        
        return value

class TaskSerialize(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['tid','uid','task_title','task_description','task_pic','create_time_stamp']
