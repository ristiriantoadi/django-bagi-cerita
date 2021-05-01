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
                next_url = request.POST['next']
                return redirect(next_url)
            except Profile.DoesNotExist:
                return redirect(f"/user/{user.username}/profile/edit")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("<h1>Wrong password or username</h1>")

        raise Http404("there is no login page--login via popup")

def register_view(request,*args, **kwargs):
    if(request.method == "POST"):
        user = User.objects.create_user(username=request.POST.get('username'), 
        password=request.POST.get('password1'))
        login(request,user)
        try:
            profile = user.profile
            return redirect("stories")
        except Profile.DoesNotExist:
            return redirect(f"user/{user.username}/profile/edit")
    raise Http404("there is no register page--register via popup")

def logout_view(request,*args, **kwargs):
    logout(request)
    next_url = request.GET['next']
    return redirect(next_url)

def user_profile_view(request,username):
    user = User.objects.filter(username=username).first()
    context = {
        "img":"profile_picture/man.svg",
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
        context['gender'] = profile.gender
        context['kota'] = profile.kota
        context['tentang_saya'] = profile.tentang_saya
        if(profile.profile_picture):
            context["img"] = profile.profile_picture
    except Profile.DoesNotExist:
        pass

    # get user stories
    stories=user.story_set.all()
    print("stories: "+str(stories))
    context['stories'] = stories

    return render(request,"user/user_profile.html",context)

def edit_user_profile_view(request,username):
    if(request.method == "POST"):
        nama_lengkap = request.POST['nama-lengkap']
        tanggal_lahir = request.POST['tanggal-lahir']
        gender = request.POST['gender']
        kota = request.POST['kota']
        tentang_saya = request.POST['tentang-saya']
        if(request.FILES):
            profile_picture = request.FILES['profile-picture']
        else:
            profile_picture=None
        try:
            profile = request.user.profile
            profile.nama_lengkap = nama_lengkap
            profile.tanggal_lahir = tanggal_lahir
            profile.gender = gender
            profile.kota = kota
            profile.tentang_saya = tentang_saya
            if(profile_picture != None):
                profile.profile_picture = profile_picture
            profile.save()
        except Profile.DoesNotExist:
            Profile.objects.create(user=request.user,profile_picture=profile_picture,kota=kota,tentang_saya=tentang_saya,gender=gender,nama_lengkap=nama_lengkap,tanggal_lahir=tanggal_lahir)
        
        return redirect(f"/user/{request.user.username}/profile")
    
    context = {
        "username":username,
        "nama_lengkap":"",
        "tanggal_lahir":"",
        "gender":"",
        "kota":"",
        "tentang_saya":"",
        "profile_picture":"-"
    }

    try:
        profile = request.user.profile
        context['nama_lengkap'] = profile.nama_lengkap
        context['tanggal_lahir'] = profile.tanggal_lahir
        context['gender'] = profile.gender
        context['kota'] = profile.kota
        context['tentang_saya']=profile.tentang_saya
        if(profile.profile_picture):
            context['profile_picture'] = profile.profile_picture
    except Profile.DoesNotExist:
        pass

    print("context: "+str(context))
    return render(request,"user/edit_user_profile.html",context)

def notifikasi_view(request,username):
    context = {
        "page":"notifikasi"
    }
    return render(request,"user/notifikasi.html",context)