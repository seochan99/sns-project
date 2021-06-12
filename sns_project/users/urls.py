from django.urls import path
from . import views

app_name ="users"
urlpattern=[
    path('mypage/',views.mypage,name="mypage"),
] 