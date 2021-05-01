from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from story.models import Story
from datetime import datetime
from django.http import Http404


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

# get story
def story_view(request,story_id):

    context={
        "id":story_id,
        "rating":10,
        "story":get_story(story_id)
    }
    return render(request,"story/story.html",context)

#post story / add story / create story
def post_story_view(request):

    if(request.method == "POST"):
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        date_posted = datetime.date(datetime.now())
        story = Story.objects.create(title=title,content=content,user=user,date_posted=date_posted)
        return redirect(f"/stories/{story.id}")

    context={
        "rating":10,                
        "page":"post_story"
    }
    return render(request,"story/posting_story.html",context)

# edit story
def edit_story_view(request,story_id):
    if(request.method == "POST"):
        story = Story.objects.get(id=story_id)
        story.title = request.POST.get('title')
        story.content = request.POST.get('content')
        story.save()
        return redirect(f"/stories/{story.id}")

    context={
        "id":story_id,
        "rating":10,
        "story":get_story(story_id),
        "page":"edit_story"
    }
    return render(request,"story/posting_story.html",context)

# delete story
def delete_story_view(request,story_id):
    # delete story
    obj =  get_object_or_404(Story,id=story_id)
    obj.delete()

    return redirect("stories")
    # return render(request,"story/posting_story.html",context)


# helper functions
def get_story(story_id):
    # get story
    try:
        story = Story.objects.get(id=story_id)
    except Story.DoesNotExist:
        raise Http404("Story does not exist")

    return story
