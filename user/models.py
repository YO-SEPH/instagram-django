from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# 모델
class User(AbstractBaseUser):
    """
    유저 프로파일 사진
    유저 닉네임        -> 화면에 표시되는 이름
    유저 이름          -> 실제 사용자의 이름
    유저 이메일 주소    -> 회원가입할때 사용하는 아이디
    유저 비밀번호
    """
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True, unique=True)
    user_id = models.CharField(max_length=30, blank=True, null=True)
    thumbnail = models.CharField(max_length=256, default='default_profile.jpg', blank=True, null=True)

    USERNAME_FIELD = 'id' # 사용자의 이름값을 'id' 필드로 사용한다는 뜻
    REQUIRED_FIELDS = ['user_id'] # 사용자 데이터를 만들 때 필요한 데이터 필드

    def __str__(self):
        return self.user_id

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'User'

