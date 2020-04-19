from django.contrib.auth.models import User
from django import forms
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model = User
        fields = ('username','email','password')


class UserProfile(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')