from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def register(request):
    if request.method == 'post':

        #* get form values
        username = request.post['username']
        email = request.post['email']
        password = request.post['password']
        repassword = request.post['repassword']

        if password == repassword:
            #* username
            if User.objects.filter(username = username).exists():
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'users/register.html')