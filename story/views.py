from django.shortcuts import render,redirect

# Create your views here.
def home_view(request,*args, **kwargs):
    return redirect("stories")
def stories_view(request):
    context={
        "page":"stories"
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
        "id":story_id
    }
    return render(request,"story/story.html",context)