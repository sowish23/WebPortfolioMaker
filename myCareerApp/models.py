# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    objects = models.Manager()
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name="USERID")
    name = models.CharField(null=True, blank=True, max_length=10, verbose_name="NAME")
    image = models.ImageField(upload_to = "static/img/profile", null=True, blank=True, default = '', verbose_name="IMAGE")
    tel = models.CharField(null=True, blank=True, max_length=12, verbose_name="TEL")
    email = models.EmailField(verbose_name="EMAIL", max_length=30, null=True, blank=True)
    birth = models.DateField(auto_now_add=False, null=True, blank=True, verbose_name="BIRTH")
    tech = models.TextField(null=True, blank=True, verbose_name="TECH")
    intro = models.TextField(null=True, blank=True, default= "안녕하세요", verbose_name="INTRO")
    career = models.TextField(null=True, blank=True, verbose_name="CAREER")
    kakaoId = models.CharField(null=True, blank=True, max_length=100, verbose_name="KAKAOID")
    github_url = models.CharField(null=True, blank=True, max_length=100, verbose_name="GITHUB")

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ProjectBoard(models.Model):
    objects = models.Manager()
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    project_title = models.CharField(null=True, blank=True, default = '', max_length=200, verbose_name="PROJECT TITLE")
    project_des = models.TextField(null=True, blank=True, default = '', verbose_name="PROJECT DESCRIPTION")
    project_url = models.TextField(null=True, blank=True, default = '', verbose_name="PROJECT URL")
    project_img = models.ImageField(upload_to = "static/img/project", null=True, blank=True, default = '', verbose_name="PROJECT IMAGE")
    project_num = models.AutoField(db_column='ProjectId', primary_key=True)