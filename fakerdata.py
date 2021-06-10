import os,django,datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE','myTask2.settings')
django.setup()
import random
from myApp2.models import User,Task
from faker import Faker
from django.utils import timezone

faker = Faker()
def create_task(N):

    for x in range(N):
        id = random.randint(1,4)
        title = faker.name()
        desc = faker.text()
        uid = User.objects.get(uid=id)
        created = datetime.datetime.now()
        data = Task(uid = uid,task_title=title,task_description=desc, create_time_stamp=created)
        data.save()
create_task(5)
print("success")

