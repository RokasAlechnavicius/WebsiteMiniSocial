from django.shortcuts import render,redirect, HttpResponse
from accounts.forms import UserRegistrationForm, EditProfileForm,UserInformationForm,EditProfileInformationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def home(request):
    return render(request,'accounts/home.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserInformationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user=user

            profile.save()

            registered=True
            return redirect('/accounts')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserRegistrationForm()
        profile_form = UserInformationForm()

    args = {'user_form':user_form,
            'profile_form':profile_form,
            'registered':registered}
    return render(request,'accounts/register_form.html',args)

@login_required
def profile(request):
    args ={'user':request.user}
    return render(request,'accounts/profile.html',args)

@login_required
def editprofile(request):
    if request.method == 'POST' :
        user_form = EditProfileForm(data = request.POST,instance = request.user)
        profile_form = EditProfileInformationForm(data=request.POST,instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = EditProfileForm(instance = request.user)
        profile_form = EditProfileInformationForm(instance=request.user)
    args = {'user_form':user_form,'profile_form':profile_form}
    return render(request,'accounts/editprofile.html',args)

@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data =request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            redirect('account/changepassword')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'accounts/changepassword.html',args)
