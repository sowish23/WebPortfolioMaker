from django.forms import ModelForm
from .models import Profile, ProjectBoard
 
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'intro', 'tel', 'email', 'birth', 'tech', 'career', 'kakaoId', 'github_url']