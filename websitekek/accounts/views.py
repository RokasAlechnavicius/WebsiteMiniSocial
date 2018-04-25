from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from accounts.forms import UserRegistrationForm, EditProfileForm,UserInformationForm,EditProfileInformationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ErrorLogging
# Create your views here.


def home(request):
    return render(request,'accounts/home.html')
def ShowLogs(request):
    queryset = ErrorLogging.objects.all().order_by('error_time')
    args = {'errors':queryset}
    return render(request,'accounts/SystemLogs.html',args)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request,user)
        return render(request,'index.html')


    return render(request,"accounts/login.html",{'form':form})



def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        # profile_form = UserInformationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username,password=password)
            login(request,new_user)
            # profile = profile_form.save(commit=False)
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            # profile.user=user
            # profile.save()
            registered=True
            return redirect('/accounts')
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()
        # profile_form = UserInformationForm()

    args = {'user_form':user_form,
            'registered':registered}
    return render(request,'accounts/register_form.html',args)


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username,password=password)
#
#         if user:
#             if user.is_active():
#                 login(request,user):
#                 return render(request,'accounts/home.html')
#             else:
#                 return HttpResponse("account is not active")
#         else:
#             print
#             return render(request)





@login_required
def profile(request):
    args ={'user':request.user}
    return render(request,'accounts/profile.html',args)

@login_required
def editprofile(request):
    if request.method == 'POST' :
        user_form = EditProfileForm(data = request.POST,instance = request.user)
        profile_form = EditProfileInformationForm(data=request.POST,instance = request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('/accounts/profile')
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = EditProfileForm(instance = request.user)
        profile_form = EditProfileInformationForm(instance = request.user.userprofile)
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
            print(form.errors)
            redirect('account/changepassword')

    else:
        form = PasswordChangeForm(request.user)
    args = {'form':form}
    return render(request,'accounts/changepassword.html',args)
