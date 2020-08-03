from django.db import models

class ProjectBoard(models.Model):
    project_title = models.CharField(default = '', max_length=200, verbose_name="프로젝트 이름")
    project_des = models.TextField(default = '')
    project_url = models.TextField(default = '')
    project_img = models.TextField(null=True)
    project_id = models.IntegerField(default = '')

class Profile(models.Model):
    name = models.CharField(max_length=10)
    image = models.TextField(null=True)
    tel = models.CharField(max_length=12)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    birth = models.TextField(null=True)
    tech = models.TextField(null=True)
    intro = models.TextField(blank=True, default= "안녕하세요")
    career = models.TextField(null=True)
    kakaoId = models.TextField(null=True)
    github_url = models.TextField(null=True)