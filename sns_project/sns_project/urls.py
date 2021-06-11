
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # settings 가져오기 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), #urls.py 관리하는법 
    #allauth의 url연결 
    path('accounts/',include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
