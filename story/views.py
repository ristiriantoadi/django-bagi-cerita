from django.shortcuts import render,redirect

# Create your views here.
def home_view(request,*args, **kwargs):
    return redirect("stories")
def stories_view(request):
    return render(request,"story/stories.html")
def popular_stories_view(request):
    return render(request,"story/popular_stories.html")
def best_stories_view(request):
    return render(request,"story/best_stories.html")
def featured_stories_view(request):
    return render(request,"story/featured_stories.html")
def story_view(request,story_id):
    context={
        "id":story_id
    }
    return render(request,"story/story.html",context)