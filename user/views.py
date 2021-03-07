from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

# Create your views here.
def login_view(request,*args, **kwargs):
    raise Http404("there is no login page--login via popup")

def register_view(request,*args, **kwargs):
    raise Http404("there is no register page--register via popup")

def user_profile_view(request,user_id):
    context = {
        "id":user_id
    }
    return render(request,"user/user_profile.html",context)

def edit_user_profile_view(request,user_id):
    context = {
        "id":user_id
    }
    return render(request,"user/edit_user_profile.html",context)