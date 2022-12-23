from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Oturum açıldı.')
            print("oturum oke")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Hatalı kullanıcı adı ya da şifre.')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Oturumunuz kapatıldı.")
        return redirect('index')

def register(request):
    if request.method == 'POST':

        #* Get form values
        username = request.POST['username']
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.post['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            #* Username Filter
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'Kullanıcı adı mevcuttur.')
                return redirect('register')
            else:
                #* E-mail Filter
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'E-mail mevcuttur.')
                    return redirect('register')
                else:
                    #* Save to User
                    user = User.objects.create_user(username=username, password=password, email=email, name=name, surname=surname)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Kullanıcı kayıt edildi.')
                    return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Parola uyumsuzluğu.')
            return redirect('register')
    else:
        return render(request, 'users/register.html')