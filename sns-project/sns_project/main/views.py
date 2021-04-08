from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request,"main/show.html")

def hello(request):
    userName = request.GET("name")
    return render(request,"main/hello.html",{"userName" : userName})