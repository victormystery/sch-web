

from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate

from django.contrib.auth import logout
# from .forms import ParentRegister
# from .models import User


# Create your views here.

def home(request, *args, **kwargs):
    return render(request, "index.html", {})

def base(request, *args, **kwargs):
    return render(request, "base.html", {})

def staff(request, *args, **kwargs):
    return render(request, 'staff.html', {})

def about(request, *args, **kwargs):
    return render(request, "about.html", {})

def detail(request, *args, **kwargs):
    return render(request, "detail.html", {})    

def admission(request, *args, **kwargs):
    return render(request, "admission.html", {})

# Create your views here.
def parent(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password1']
        if password1 == password2:

            if User.objects.filter(email=mail).exists():
                messages.info(request, 'Email Taken')
            elif User.objects.filter(username=name).exists():
                print('username Taken')
            else:
                user = User.objects.create_user(
                    username=name, email=mail, password=password1)
                user.save()
                return redirect("main")

        else:
            messages.error(request, 'password does not match')
        return redirect("parent")

    else:
        return render(request, "parent.html")


def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("base")

        else:
            messages.info(request, 'invalid credentials')
            return redirect("account")

    else:
        return render(request, "login.html")




def logoutUser(request):
    logout(request)
    return redirect("account")



def change_password(request):
    return render(request, "")