from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):    
    use_in_migrations = True
    def create_user(self, email, nickname, password=None):
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email, nickname, password ):
        user = self.create_user(
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 

class User(AbstractBaseUser,PermissionsMixin): 
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )     
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'nickname'    
    REQUIRED_FIELDS = ['email']

class Profile(models.Model):
    objects = models.Manager()
    # user_id = models.CharField(null=False, max_length=10, unique=True, verbose_name="ID")
    # user_password = models.CharField(null=False, max_length=15, verbose_name="PASSWORD")
    name = models.CharField(null=False, max_length=10, verbose_name="NAME")
    image = models.ImageField(upload_to = "static/img/profile", null=False, default = '', verbose_name="IMAGE")
    tel = models.CharField(null=False, max_length=12, verbose_name="TEL")
    email = models.EmailField(verbose_name="EMAIL", max_length=255, null=False )
    birth = models.DateField(auto_now_add=False, null=True, verbose_name="BIRTH")
    tech = models.TextField(null=True, verbose_name="TECH")
    intro = models.TextField(null=True, blank=True, default= "안녕하세요", verbose_name="INTRO")
    career = models.TextField(null=True, verbose_name="CAREER")
    kakaoId = models.CharField(null=True, max_length=100, verbose_name="KAKAOID")
    github_url = models.CharField(null=True, max_length=100, verbose_name="GITHUB")

class ProjectBoard(models.Model):
    objects = models.Manager()
    project_title = models.CharField(null=False, default = '', max_length=200, verbose_name="PROJECT TITLE")
    project_des = models.TextField(null=False, default = '', verbose_name="PROJECT DESCRIPTION")
    project_url = models.TextField(null=False, default = '', verbose_name="PROJECT URL")
    project_img = models.ImageField(upload_to = "static/img/project", null=False, default = '', verbose_name="PROJECT IMAGE")
    project_id = models.IntegerField(null=True, default = 0, verbose_name="PROJECT ID")