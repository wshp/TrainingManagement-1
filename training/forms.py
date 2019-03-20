from django.forms import forms,ModelForm
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','email')

class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')