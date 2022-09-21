from re import template
from django.shortcuts import render, redirect
#now inherit the form that we have just created
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
from django.views.generic import FormView
#to create user form we are importing some packages
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in !') #{username}
            return redirect('login-app')
             #return redirect('login-app')      
    else:

        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request, 'users_app/register.html',{'form': form})




@login_required
def profile(request):
    if request.method == 'POST':
    #to update the profile page
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                  request.FILES, 
                                  instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('profile-app')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form= ProfileUpdateForm(instance = request.user.profile)
        
    


    context = {

        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users_app/profile.html',context) 


