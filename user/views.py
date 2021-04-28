from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, Http404, HttpResponse
from django.contrib.auth.models import User
from user.models import Profile
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def login_view(request,*args, **kwargs):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect
            # check if user already have profile or not
            try:
                user.profile
                return redirect("stories")
            except Profile.DoesNotExist:
                return redirect(f"/user/{user.username}/profile/edit")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("<h1>Wrong password or username</h1>")

        raise Http404("there is no login page--login via popup")

def register_view(request,*args, **kwargs):
    if(request.method == "POST"):
        user = User.objects.create_user(request.POST.get('username'), 
        request.POST.get('password1'))
        login(request,user)
        return redirect("stories")
    raise Http404("there is no register page--register via popup")

def logout_view(request,*args, **kwargs):
    logout(request)
    return redirect("stories")

def user_profile_view(request,username):
    user = User.objects.filter(username=username).first()
    print(user)
    context = {
        "img":"user/123/something.jpg",
        "nama_lengkap":"-",
        "tanggal_lahir":"-",
        "gender":"-",
        "kota":"-",
        "tentang_saya":"-",
        "page":"profil",
        "user":username
    }
    try:
        profile = user.profile
        context['nama_lengkap'] = profile.nama_lengkap
        context['tanggal_lahir'] = profile.tanggal_lahir
        # context['gender'] = profile.gender
        # context['kota'] = profile.kota
        # context['tentang_saya'] = profile.tentang_saya
    except Profile.DoesNotExist:
        pass
    
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