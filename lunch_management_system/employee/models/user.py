from rest_framework_simplejwt.tokens import RefreshToken
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .user_manager import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, blank=False)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')
        ordering = ['id']
    
    def __str__(self) -> str:
         return self.username
        

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "token": str(refresh.access_token),
            "refresh_token": str(refresh)
        }
        