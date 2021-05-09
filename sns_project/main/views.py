from django.shortcuts import render

# Create your views here.

def showmain(request):
    return render(request, 'main/mainpage.html')
  
def introduceMe(request): #소개 페이지 
    return render(request, 'main/introduce.html')

def photoMe(request): # 사진 
    return render(request, 'main/photo.html')
 
def profileMe(request): # 프로파일 !
    return render(request, 'main/profile.html')

def home(request):
    userName = request.GET['name']
    return render(request, 'main/home.html',{'userName':userName})