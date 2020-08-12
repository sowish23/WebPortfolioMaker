from django.forms import ModelForm
from .models import Profile, ProjectBoard
 
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'intro', 'tel', 'email', 'birth', 'tech', 'career', 'kakaoId', 'github_url']

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectBoard
        fields = ['project_title', 'project_url', 'project_des', 'project_img']