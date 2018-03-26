from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2')

class UserInformationForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('description','city','phonenumber')

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
        )

class EditProfileInformationForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('description','city','phonenumber')
