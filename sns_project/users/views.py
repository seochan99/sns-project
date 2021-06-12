from django.shortcuts import render
from main.models import Post
from django.contrib.auth.models import User 

def mypage(request):
    user = request.user
    posts = Post.objects.filter(writer = user) #로그인한 유저이름과 글 작성자 이름이 동일한 글 필터링한다.
    return render(request,'user/mypage.html',{'posts':posts})
