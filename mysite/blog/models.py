from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
# 이 모델의 저자는 AUTH_USER_MODEL을 참조하는 ForeignKey 객체이다. 
# 저자가 삭제되면, on_delete 옵션에 의해 이 모델도 삭제된다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)# 제목은 최대 200글자의 문자열이다.
    text = models.TextField()# 텍스트는 긴 문자열이다.
    created_date = models.DateTimeField(
            default=timezone.now)# 작성일은 기본값으로 현재 시간이 설정된다.
    published_date = models.DateTimeField(
            blank=True, null=True)# 게시일은 빈 값이나 null 값이 허용된다.

# 'publish' 메소드는 게시일을 현재 시간으로 설정하고 모델을 저장한다.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# 모델의 제목을 반환하는 '__str__' 메소드
    def __str__(self):
        return self.title