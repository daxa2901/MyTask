from django.db import router
from django.urls import path,include
from myApp2.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('task',views.TaskView, basename='task')
router.register('user',views.UserView, basename='user')
urlpatterns = [
    path('',include(router.urls))
]




