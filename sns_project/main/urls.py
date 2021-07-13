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
    path("editComment/<str:post_id>/<str:com_id>",comment_edit,name="comment_edit"),
    path("update/<str:id>",update,name="update"),
    path("delete/<str:id>",delete,name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path('updateComment/<str:post_id>/<str:com_id>',update_comment, name="update_comment"),
    path('deleteComment/<str:com_id>',delete_Comment, name = "delete_Comment"),
]