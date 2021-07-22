from django.urls import path
from . import views

app_name ="users"
urlpatterns=[
    path('mypage/<int:id>',views.mypage,name="mypage"),
    path('follow<int:id>',views.follow, name="follow"),
] 