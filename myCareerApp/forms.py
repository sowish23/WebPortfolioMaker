from django.forms import ModelForm
from .models import Profile, ProjectBoard
from .widgets import DatePickerWidget

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'intro', 'tel', 'email', 'birth', 'tech', 'career', 'kakaoId', 'github_url']
        widgets = {
            'birth' : DatePickerWidget
        }

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectBoard
        fields = ['project_title', 'project_url', 'project_des', 'project_img']