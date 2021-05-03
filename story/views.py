from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from story.models import Story,Comment,Tag
from datetime import datetime
from django.http import Http404


# Create your views here.
def home_view(request,*args, **kwargs):
    return redirect("stories")

# get stories
def stories_view(request):

    # get all stories
    stories = get_stories()
    # get_story(story.)
    # stories_returned=[]
    # for story in stories:
    #     story = get_story(story.id)
    # stories = calculate_stories_rating(stories)

    context={
        "page":"stories",
        "stories": stories
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
        return redirect(f"/stories/{story_id}")

    context={
        "id":story_id,
        "rating":10,
        "story":get_story(story),
        "comments":get_comments(story_id),
        "have_commented":"False"
    }
    for comment in context['comments']:
        print("comment: "+str(comment))
        if(comment.user.id == request.user.id):
            context['have_commented']="True"
    
    return render(request,"story/story.html",context)

#post story / add story / create story
def post_story_view(request):

    if(request.method == "POST"):
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        date_posted = datetime.date(datetime.now())
        story = Story.objects.create(title=title,content=content,user=user,date_posted=date_posted)
        # story.tags.create()
        tags = request.POST.getlist('tag[]')
        for tag in tags:
            name = tag
            tag_object = Tag.objects.create(name=tag)
            tag_object.stories.add(story)
        
        return redirect(f"/stories/{story.id}")

    context={
        "rating":10,                
        "page":"post_story"
    }
    return render(request,"story/posting_story.html",context)

# edit story
def edit_story_view(request,story_id):
    story = Story.objects.get(id=story_id)
    if(request.method == "POST"):
        story.title = request.POST.get('title')
        story.content = request.POST.get('content')
        story.tag_set.clear()
        story.save()

        tags = request.POST.getlist('tag[]')
        for tag in tags:
            name = tag
            try:
                tag_object = Tag.objects.get(name=name)
            except Tag.DoesNotExist:
                tag_object = Tag.objects.create(name=name)
            tag_object.stories.add(story)
                
        return redirect(f"/stories/{story.id}")

    context={
        "id":story_id,
        "rating":10,
        "story":get_story(story),
        "page":"edit_story"
    }
    return render(request,"story/posting_story.html",context)

# delete story
def delete_story_view(request,story_id):
    # delete story
    obj =  get_object_or_404(Story,id=story_id)
    obj.delete()

    return redirect("stories")

# add comments
def add_comment_view(request,story_id):
    
    # add comment
    return redirect("stories")
    


# helper functions
def get_stories():
    stories = Story.objects.all()
    returned_stories=[]
    for story in stories:
        story = get_story(story)
        returned_stories.append(story)
    return returned_stories

def get_story(story):
    # get story
    # try:
    #     # story = Story.objects.get(id=story_id)
    #     story.tags = story.tag_set.all()
    #     story = calculate_story_rating(story)
    # except Story.DoesNotExist:
    #     raise Http404("Story does not exist")

    # get the tags and the rating
    story.tags = story.tag_set.all()
    story = calculate_story_rating(story)
    return story

def get_comments(story_id):
    story_comments = Story.objects.get(id=story_id).comment_set.filter(replied_comment_id=0)
    return iterate_through_comments_and_get_replies(story_comments)

def get_replies(comment_id):
    comment_replies = Comment.objects.filter(replied_comment_id=comment_id) 
    return iterate_through_comments_and_get_replies(comment_replies)

def iterate_through_comments_and_get_replies(comments):
    # comments_to_return=[]
    for comment in comments:
        # comment_item={
        #     "comment":comment,
        #     "replies": get_replies(comment.id)
        # }
        comment.replies = get_replies(comment.id)
        # comments_to_return.append(comment_item)
    return comments

    
def calculate_stories_rating(stories):
    for story in stories:
        story = calculate_story_rating(story)
    return stories

def calculate_story_rating(story):
    # aggregate the rating in each comment for ALL comments
    comments = story.comment_set.filter(replied_comment_id=0)
    story_rating=0
    for comment in comments:
        story_rating+=comment.rating
    story.rating = story_rating
    return story