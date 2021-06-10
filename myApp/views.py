from django.shortcuts import render
from .models import MyList
from myApp.templatetags import get_Dict
# Create your views here.

def mylist(request):
    l1 = MyList.objects.filter(ParentId=None)
    l2 = MyList.objects.all().exclude(ParentId=None)
    l3 = MyList.objects.select_related('ParentId')
    dict = {}
    for data in l2:
            if data.ParentId.SINO not in dict.keys():
                dict[data.ParentId.SINO] = [data]
                 
            else:
                
                dict[data.ParentId.SINO].append(data) 
    context = {'dict':dict, 'list1':l1}
    return render(request,"mylist.html", context)


