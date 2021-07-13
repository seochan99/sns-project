from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/",blank=True,null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10] ## 적절량 짜르기 

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# 클래스 머델 생성, migrate해주기, superuser만들기, 블로그 쓰기, 블로그 제목 뜨게 만들기, 
# python manage.py makemigrations 모델변경사항 저장
#python manage.py migrate -> 데이터 베이스에 적용 