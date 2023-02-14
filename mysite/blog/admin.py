#'django.contrib.admin' 모듈에서 'admin' 이라는 객체를 가져온다.
from django.contrib import admin
#'models' 모듈에서 'Post' 모델을 가져온다.
from .models import Post

# Register your models here.
#모델을 등록한다.
admin.site.register(Post)