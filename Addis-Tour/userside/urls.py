from django.urls import path
from . import views

urlpatterns=[
    path('userLogin',views.ulogin,name="userLogin"),
    path('userReg',views.userReg,name="userReg"),
]