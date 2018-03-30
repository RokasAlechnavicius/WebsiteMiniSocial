from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile
from django.contrib.auth import get_user_model,authenticate

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    #checks if valid
    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user_qs = User.objects.filter(username=username)
        if username and password:
            user = authenticate(username=username,password=password)
            if user_qs.count()==0:
                raise forms.ValidationError("User with this name does not exist")
            if not user:
                raise forms.ValidationError("password is incorrect")
            if not user.is_active:
                raise forms.ValidationError("this user is no longer active")
            return super(UserLoginForm,self).clean(*args,**kwargs)

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
