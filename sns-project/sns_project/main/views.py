from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainPage.html') 

def show(request):
    userName = request.GET['name'] # 대괄호다 ! 
    return render(request,'main/show.html',{'userName': userName})