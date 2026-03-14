from django.shortcuts import render, redirect
from . forms import RegistrationForm
from .models import Account
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # When using django forms, you need to use cleaned_data to get the values from the request
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
    # next is to create user which is from the Django user which is from MyAccountManager class
            
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            # since the MyAccountManager class does not include phonenumber, we now add phonenumber after creating the user
            user.phone_number = phone_number
            
            #then save the user
            user.save()
            messages.success(request, 'Registration successful!')
            return redirect('register')       
    else:
        form = RegistrationForm()
        
    context = {
            'form': form
        }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')
