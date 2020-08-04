# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models

# class UserManager(BaseUserManager):    
#     use_in_migrations = True
#     def create_user(self, email, nickname, password=None):
#         if not email :            
#             raise ValueError('must have user email')        
#         user = self.model(            
#             email = self.normalize_email(email),            
#             nickname = nickname        
#         )
#         user.set_password(password)        
#         user.save(using=self._db)        
#         return user     
#     def create_superuser(self, email, nickname,password ):
#         user = self.create_user(
#             email = self.normalize_email(email),            
#             nickname = nickname,            
#             password=password        
#         )        
#         user.is_admin = True        
#         user.is_superuser = True        
#         user.is_staff = True        
#         user.save(using=self._db)        
#         return user 

class ProjectBoard(models.Model):
    project_title = models.CharField(null=False, default = '', max_length=200, verbose_name="프로젝트 이름")
    project_des = models.TextField(null=False, default = '', verbose_name="프로젝트 설명")
    project_url = models.TextField(null=False, default = '', verbose_name="프로젝트 링크")
    project_img = models.TextField(null=True, verbose_name="프로젝트 사진")
    project_id = models.IntegerField(null=False, default = '', verbose_name="프로젝트 번호")

class Profile(models.Model):
    user_id = models.CharField(null=False, max_length=10, verbose_name="아이디")
    user_password = models.CharField(null=False, max_length=15, verbose_name="비밀번호")
    name = models.CharField(null=False, max_length=10, verbose_name="이름")
    image = models.TextField(null=True, verbose_name="프로필 사진")
    tel = models.CharField(null=False, max_length=12, verbose_name="전화번호")
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
        null=False, 
    )
    birth = models.TextField(null=True, verbose_name="생년월일")
    tech = models.TextField(null=True, verbose_name="기술")
    intro = models.TextField(null=True, blank=True, default= "안녕하세요", verbose_name="자기소개")
    career = models.TextField(null=True, verbose_name="경력")
    kakaoId = models.TextField(null=True, verbose_name="카카오톡아이디")
    github_url = models.TextField(null=True, verbose_name="깃허브")