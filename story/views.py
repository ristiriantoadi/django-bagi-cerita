from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from story.models import Story

# Create your views here.
def home_view(request,*args, **kwargs):
    return redirect("stories")

def stories_view(request):

    # get all stories
    stories = Story.objects.all()

    # form = UserCreationForm()
    context={
        "page":"stories",
        "stories": stories
        # "form":form
    }
    return render(request,"story/stories.html",context)

def popular_stories_view(request):
    context={
        "page":"popular"
    }
    return render(request,"story/stories.html",context)

def best_stories_view(request):
    context={
        "page":"best"
    }
    return render(request,"story/stories.html",context)
    
def featured_stories_view(request):
    context={
        "page":"featured"
    }
    return render(request,"story/stories.html",context)

def story_view(request,story_id):
    context={
        "id":story_id,
        "rating":10
    }
    return render(request,"story/story.html",context)

def post_story_view(request):
    context={
        "rating":10
    }
    return render(request,"story/posting_story.html",context)

def edit_story_view(request,story_id):
    context={
        "id":story_id,
        "rating":10
    }
    return render(request,"story/posting_story.html",context)