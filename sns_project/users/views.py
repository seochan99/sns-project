from django.shortcuts import get_object_or_404, redirect, render
from main.models import Post
from django.contrib.auth.models import User 

def mypage(request, id):
    user = get_object_or_404(User,pk=id)
    context={
        'user':user,
        'posts':Post.objects.filter(writer=user),
        'followings':user.profile.followings.all(),
        'followers':user.profile.followers.all(),
    }
    return render(request,'users/mypage.html',context) 

def follow(request,id):
    user = request.user #로그인한 유저(A)
    followed_user = get_object_or_404(User,pk=id) #팔로우/언팔로우 할 유저 (B)
    is_follower = user.profile in followed_user.profile.followers.all() #B의 팔로워 목록에 A가 있는지 판단 
    if is_follower:
        user.profile.followings.remove(followed_user.profile) #remove -> A의 팔로잉 목록에서 B삭제 
    else:
        user.profile.followings.add(followed_user.profile) #A팔로잉 목록에서 B추가 
    return redirect('users:mypage',followed_user.id)