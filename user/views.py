from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def login_view(request,*args, **kwargs):
    raise Http404("there is no login page--login via popup")

def register_view(request,*args, **kwargs):
    if(request.method == "POST"):
        user = User.objects.create_user(request.POST.get('username'), 
        request.POST.get('password'))
        return redirect("stories")
def user_profile_view(request,username):
    context = {
        "img":"user/123/something.jpg",
        "page":"profil"
    }
    return render(request,"user/user_profile.html",context)

def edit_user_profile_view(request,username):
    context = {
        "username":username
    }
    return render(request,"user/edit_user_profile.html",context)

def notifikasi_view(request,username):
    context = {
        "page":"notifikasi"
    }
    return render(request,"user/notifikasi.html",context)