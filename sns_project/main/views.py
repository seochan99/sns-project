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

def edit(request, id):
    edit_blog = Post.objects.get(id=id)
    return render(request,"main/edit.html",{"Post":edit_Post})

def update(request,id):
    update_Post = Post.objects.get(id=id)
    update_Post.title = request.POST['title']
    update_Post.writer = request.POST['writer']
    update_Post.pub_date = timezone.now()
    update_Post.body = request.POST['body']
    update_Post.image = request.FILES['image']
    update_Post.save()
    return redirect('main:detail', update_Post.id)

def delete(request, id):
    delete_Post = Post.objects.get(id=id) #모든 객체 가지고온다 
    delete_Post.delete() ## 삭제 ~ 
    return redirect("main:posts") #삭제후 보여지는 페이지 이동 