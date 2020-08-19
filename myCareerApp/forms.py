from django.forms import ModelForm
from django import forms
from .models import Profile, ProjectBoard
from .widgets import DatePickerWidget

class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'name', 'intro', 'tel', 'email', 'birth', 'tech', 'career', 'kakaoId', 'github_url']
        widgets = {
            'birth' : DateInput()
        }

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectBoard
        fields = ['project_title', 'project_url', 'project_des', 'project_img']