from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Django User 모델 사용법
# 1) models.User 와 onetoone 관계인 모델(ex. Profile) 생성
# 2) models.AbstratUser 상속
# 3) models.AbstractBaseUser 상속
#
# 2, 3번을 사용하려면 첫 번째 마이그레이션을 적용 하기 전에 사용자 지정 사용자 모델을 생성해야 한다.

'''
class CustomAbstractUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
'''

class CustomAbstractBaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
