from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain,name="show"),
    path('home',home,name="home"),
    path("profileMe",profileMe, name="profileMe"),
    path("photoMe",photoMe,name="photoMe"),
    path("introduceMe",introduceMe, name="introduceMe"),
    path('<str:id>',detail, name="detail"),
    path('new/',new, name="new"),
    path('create/',create, name="create"),
    path("edit/<str:id>",edit,name="edit"),
    path("update/<str:id>",update,name="update"),
    path("delete/<str:id>",delete,name="delete"),
]