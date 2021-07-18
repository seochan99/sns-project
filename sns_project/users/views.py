from django.shortcuts import get_object_or_404, render
from main.models import Post
from django.contrib.auth.models import User 

def mypage(request, id):
    user = get_object_or_404(User,pk=id)
    context={
        'user':user,
        'posts':Post.objects.filter(writer=user),
    }
    return render(request,'users/mypage.html',context) 
