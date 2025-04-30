from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.

def login_(request):
    context={}
    if request.method == 'POST':
        username_data=request.POST['username']
        password_data=request.POST['password']
        user=authenticate(username=username_data,password=password_data)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['wrong_credentials']=True
    return render(request,'login_.html',context)


def registration(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        try:
            username_existed=User.objects.get(username=username)
            return render(request, 'register.html', {'username_existed':username_existed})
        except:
            u=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=username)
            u.set_password(password)
            u.save()
        return redirect('login_')
    return render(request , 'register.html')

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    return render(request , 'profile.html')



@login_required(login_url='login_')
def change_password(request):
    context={}
    if request.method == 'POST':
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']

        if not check_password(old_password, request.user.password):
            context['error']='old password is incorrect'
        elif new_password != confirm_password:
            context['error']='New password does not match'
        else:
            request.user.set_password(new_password)
            request.user.save()
            #user for a keep user login after change password
            update_session_auth_hash(request,request.user)
            context['success']='login successfully'
            return redirect('home')
    return render(request ,'change_password.html',context)


def update_profile(request):
    if request.method == 'POST':
        user=request.user
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')

        user.firstname=firstname
        user.lastname=lastname
        user.email=email
        user.username=username
        user.save()
        messages.success(request, 'profile update successfully')
        return redirect('profile')
    return render(request , 'update_profile.html')


