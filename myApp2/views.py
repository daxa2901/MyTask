from .models import User,Task
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
import requests
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password

from .serialize import TaskSerialize, UserSerialize
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import api_view

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialize


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialize

@api_view(['POST'])
def saveuser(request):
    if request.method == 'POST':
        serialze = UserSerialize(data=request.data)
        if serialze.is_valid():
            serialze.save()
            return Response(serialze.data,status.HTTP_201_CREATED)
        return Response(serialze.data,status.HTTP_400_BAD_REQUEST)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        dt = request.POST['dt']
        pass1 =make_password(password)
        data= {'username':username,'join_date':dt,'password':pass1}
        headers={'Content-Type':'application/json'}
        read = requests.post('http://127.0.0.1:8000/insertuserapi',json=data,headers=headers)
        #users =User(username=username, join_date=dt,password=password)
        #users.save()
        print(read)
    
    return render(request,'signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        pasword = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            user = False
        if user:
            flag =check_password(pasword,user.password)
            if flag:
                messages.success(request,"You Logged In Successfullyy..!!")
                return redirect('taskcreate')
            else:
                messages.error(request,"username or password inccorect..!!")
                return render(request,'login.html')
        else:
            messages.error(request,"username or password inccorect..!!")
            return render(request,'login.html')
            
    else:
        return render(request,'signin.html')

def taskcreate(request):
    if request.method =='POST':
        uid = request.POST['uid']
        tasktitle = request.POST['tasktitle']
        taskdesc = request.POST['taskdesc']
        dt = request.POST['dt']
        taskpic  = request.FILES.get('taskpic')
    
        id = User.objects.get(uid=uid)
        if taskpic:
            fs=FileSystemStorage()
            filename = fs.save(taskpic.name,taskpic)
            url = fs.url(filename)
            task = Task(uid = id, task_title = tasktitle, task_description=taskdesc,task_pic = url, create_time_stamp = dt)
            task.save()
            messages.success(request,"Task Created Successfullyy..!!")
        else:
            task = Task(uid = id, task_title = tasktitle, task_description=taskdesc,create_time_stamp = dt)
            task.save()
            messages.success(request,"Task Created Successfullyy..!!")
        return render(request,'signin.html')



    else:
        data = User.objects.all()
        context = {'data':data}
        return render(request,"taskcreate.html",context)

def tasklist(request):
    data = Task.objects.all()
    paginator = Paginator(data,5, orphans=1)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    context = {'data':page_obj}

    return render(request,"tasklist.html",context)



