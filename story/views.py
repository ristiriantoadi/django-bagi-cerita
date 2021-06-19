from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from story.models import Story,Comment,Tag
from bagicerita.helpers import get_points,get_stories,get_story,get_comments,get_all_tags,story_add_tags,pagination,count_words
from datetime import datetime
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request,*args, **kwargs):
    return redirect("stories")

# get stories
# search = {"search_by":"tag","key":"something"} or {"search_by":"judul","key":"something"}
def stories_view(request):

    context={
        "page":"stories"
    }
    
    # get all stories
    stories = get_stories()

    # filter by tag
    if(request.GET.get('tag')):
        tag = request.GET.get('tag')
        stories = get_stories(search={"search_by":"tag","key":tag})
        context["page"] = "search-by-tag"
        context["tag"] = tag
    #filter by judul
    elif(request.GET.get("judul")):
        judul = request.GET.get("judul")
        stories = get_stories(search={"search_by":"judul","key":judul})
        context["page"] = "search-by-judul"
        context["judul"] = judul
    
    # pagination
    stories = pagination(stories, request)

    context["stories"] = stories

    return render(request,"story/stories.html",context)

# get popular stories
def popular_stories_view(request):
    stories = get_stories(category="popular")
    stories = pagination(stories, request)
    context={
        "page":"popular",
        "stories": stories
    }
    print("stories: "+str(context["stories"]))
    return render(request,"story/stories.html",context)

# get best stories
def best_stories_view(request):
    stories = get_stories(category="best")
    stories = pagination(stories, request)
    context={
        "page":"best",
        "stories": stories
    }
    return render(request,"story/stories.html",context)

# get featured stories    
def featured_stories_view(request):
    # context={
    #     "page":"featured",
    #     "stories": get_stories(category="featured")
    # }
    stories = get_stories(category="featured")
    stories = pagination(stories, request)
    context={
        "page":"best",
        "stories": stories
    }
    return render(request,"story/stories.html",context)

# get story  / story view
def story_view(request,story_id):

    story = Story.objects.get(id=story_id)

    # add comment or reply
    if(request.method == "POST"):
        rating=0
        if(request.POST.get("rating")):
            rating = request.POST.get('rating')
        content = request.POST.get('content') 
        user = request.user
        replied_comment_id = 0
        if(request.POST.get('replied_comment_id')):
            replied_comment_id = int(request.POST.get('replied_comment_id'))
        obj = Comment.objects.create(rating=rating,content=content,user=user,replied_comment_id=replied_comment_id,story=story)

        # add 5 points for original comment
        if(replied_comment_id == 0):
            profile = user.profile
            profile.points+=5
            profile.save()

        return redirect(f"/stories/{story_id}")

    context={
        "id":story_id,
        # "rating":10,
        "story":get_story(story),
        "comments":get_comments(story_id),
        "have_commented":"False"
    }
    for comment in context['comments']:
        print("comment: "+str(comment))
        if(comment.user.id == request.user.id):
            context['have_commented']="True"
    
    return render(request,"story/story.html",context)

#post story / add story / create story / insert story
@login_required
def post_story_view(request):

    if(request.method == "POST"):
        title = request.POST.get('title')
        content = request.POST.get('content')
        words_count=count_words(content)
        user = request.user
        date_posted = datetime.now()
        story = Story.objects.create(words_count=words_count,title=title,content=content,user=user,date_posted=date_posted)
        story_add_tags(request.POST.getlist('tag[]'), story)

        # minus 20 points
        profile = user.profile
        profile.points -=20
        profile.save()
        

        return redirect(f"/stories/{story.id}")

    context={
        "rating":request.user.profile.points,                
        "page":"post_story",
        "tags":get_all_tags()
    }
    return render(request,"story/posting_story.html",context)

# edit story
@login_required
def edit_story_view(request,story_id):
    story = Story.objects.get(id=story_id)
    if(request.method == "POST"):
        story.title = request.POST.get('title')
        story.content = request.POST.get('content')
        story.words_count=count_words(story.content)
        story.tag_set.clear()
        story.save()

        story_add_tags(request.POST.getlist('tag[]'), story)
                
        return redirect(f"/stories/{story.id}")

    context={
        "id":story_id,
        "rating":10,
        "story":get_story(story),
        "page":"edit_story",
        "tags":get_all_tags()
    }
    return render(request,"story/posting_story.html",context)

# delete story
@login_required
def delete_story_view(request,story_id):
    # delete story
    obj =  get_object_or_404(Story,id=story_id)
    obj.delete()

    return redirect("stories")

# add comments
@login_required
def add_comment_view(request,story_id):
    
    # add comment
    return redirect("stories")
    


