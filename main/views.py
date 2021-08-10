from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import json

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
    all_comments = post.comments.all().order_by('-create_at')
    return render(request,'main/detail.html',{'post':post, 'comments':all_comments})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_post =Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image') #이미지 
    new_post.save()
    return redirect('main:detail',new_post.id)   

def edit(request, id):
    edit_Post = Post.objects.get(id=id)
    return render(request,"main/edit.html",{"Post":edit_Post})

#댓글 수정하기 
def edit_comment(request, post_id, com_id):
    edit_post=Post.objects.get(id=post_id)
    edit_comment=Comment.objects.get(id=com_id)
    return render(request, 'main/edit_comment.html',{'post': edit_post, 'comment':edit_comment})


#댓글 업데이트 시키기
def update_comment(request,post_id,com_id):
    if request.method =='POST':
        post= get_object_or_404(Post,pk=post_id)
        comment=Comment.objects.filter(pk=com_id)
        curUser=request.user
        com_content=request.POST.get('content')
        comment.update(content=com_content,writer=curUser,post=post)
    return redirect('main:detail',post_id)

#업데이트
def update(request,id):
    update_Post = Post.objects.get(id=id)
    update_Post.title = request.POST['title']
    update_Post.writer = request.user
    update_Post.pub_date = timezone.now()
    update_Post.body = request.POST['body']
    # update_Post.image = request.FILES['image']
    update_Post.save()
    return redirect('main:detail', update_Post.id)

def delete(request, id):
    delete_Post = Post.objects.get(id=id) #모든 객체 가지고온다 
    delete_Post.delete() # 삭제 ~ 
    return redirect("main:profileMe") #삭제후 보여지는 페이지 이동 

#댓글 삭제 함수 
def delete_Comment(request,com_id):
    delete_comment = Comment.objects.get(id=com_id)
    delete_comment.delete()
    return redirect('main:profileMe')

def create_comment(request, post_id):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=post_id)
		current_user = request.user
		comment_content = request.POST.get('content')
		Comment.objects.create(content=comment_content, writer=current_user, post=post)
	return redirect('main:detail', post_id)    


@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    
    context = {
        "like_count":post.like_count,
        "result":result
    }

    return HttpResponse(json.dumps(context), content_type="application/json")

@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    
    context = {
        "dislike_count":post.dislike_count,
        "result":result
    }

    return HttpResponse(json.dumps(context), content_type="application/json")