from myApp2.models import User,Task
from myApp2.api.serializers import UserSerialize,TaskSerialize
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialize

class MyPageNumberPagination(PageNumberPagination):
    page_size=5
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialize
    pagination_class = MyPageNumberPagination