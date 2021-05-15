from django.shortcuts import render,redirect, get_object_or_404
from .models import Post 
from django.utils import timezone


def showmain(request):
    return render(request, 'main/mainpage.html')
  
def introduceMe(request): #소개 페이지 
    return render(request, 'main/introduce.html')

def photoMe(request): # 사진 
    return render(request, 'main/photo.html')
 
def profileMe(request): # 프로파일 !
    posts = Post.objects.all()
    return render(request, 'main/profile.html',{'posts':posts})

def home(request):
    userName = request.GET['name']
    return render(request, 'main/home.html',{'userName':userName})

def detail(request,id):
    post = get_object_or_404(Post,pk = id) #id로 각 개체 구분, post에 페이지 가져와서 저장
    return render(request,'main/detail.html',{'post':post}) # 포스트가 페이지 가져옴 

def new(request):
    return render(request,'main/new.html')

def create(request):

    new_post =Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail',new_post.id)   
