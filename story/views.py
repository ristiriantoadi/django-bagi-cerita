from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from story.models import Story,Comment,Tag
from bagicerita.helpers import get_points,get_stories,get_story,get_comments,get_all_tags,story_add_tags
from datetime import datetime
from django.http import Http404


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
    
    context["stories"] = stories

    return render(request,"story/stories.html",context)

# get popular stories
def popular_stories_view(request):
    context={
        "page":"popular",
        "stories": get_stories(category="popular")
    }
    print("stories: "+str(context["stories"]))
    return render(request,"story/stories.html",context)

# get best stories
def best_stories_view(request):
    context={
        "page":"best",
        "stories": get_stories(category="best")
    }
    return render(request,"story/stories.html",context)

# get featured stories    
def featured_stories_view(request):
    context={
        "page":"featured",
        "stories": get_stories(category="featured")
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

#post story / add story / create story
def post_story_view(request):

    if(request.method == "POST"):
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        date_posted = datetime.date(datetime.now())
        story = Story.objects.create(title=title,content=content,user=user,date_posted=date_posted)
        
        story_add_tags(request.POST.getlist('tag[]'), story)

        return redirect(f"/stories/{story.id}")

    context={
        "rating":get_points(request.user),                
        "page":"post_story",
        "tags":get_all_tags()
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
# def get_stories(user=None,category="all",search=None):

#     # search = {"search_by":"tag","key":"something"} or {"search_by":"judul","key":"something"}

#     if(user):
#         stories = Story.objects.filter(user=user)
#     else:
#         stories = Story.objects.all()
        
#         # filter stories by judul
#         # if(search):
#         #     if(search["search_by"] == "judul"):
#         #         stories = Story.objects.filter(title=search["key"])
#         #         print("stories by judul: "+str(stories))
#     returned_stories=[]
#     for story in stories:
#         story = get_story(story)

#         # filter stories by tag or judul
#         if(search):
#             if(search["search_by"] == "tag"):
#                 if len(story.tag_set.filter(name=search["key"])) != 0:
#                     returned_stories.append(story)
#             else:
#                 # if story.title == search["key"]
#                 if search["key"].lower() in story.title.lower():
#                     returned_stories.append(story)
#         else:        
#             # filter stories by category
#             if(category == "all"):
#                 returned_stories.append(story)
#             elif(category == "popular"):
#                 if(story.rating >= 35 and story.rating <=50):
#                     returned_stories.append(story)
#             elif(category=="best"):
#                 if(story.rating >= 51 and story.rating <=100):
#                     returned_stories.append(story)
#             else:
#                 if(story.rating>100):
#                     returned_stories.append(story)
#     return returned_stories

# def get_story(story):
#     # get the tags and the rating
#     story.tags = story.tag_set.all()
#     story = calculate_story_rating(story)
#     return story

# def get_comments(story_id):
#     story_comments = Story.objects.get(id=story_id).comment_set.filter(replied_comment_id=0)
#     return iterate_through_comments_and_get_replies(story_comments)

# def get_replies(comment_id):
#     comment_replies = Comment.objects.filter(replied_comment_id=comment_id) 
#     return iterate_through_comments_and_get_replies(comment_replies)

# def iterate_through_comments_and_get_replies(comments):
#     # comments_to_return=[]
#     for comment in comments:
#         # comment_item={
#         #     "comment":comment,
#         #     "replies": get_replies(comment.id)
#         # }
#         comment.replies = get_replies(comment.id)
#         # comments_to_return.append(comment_item)
#     return comments

    
# def calculate_stories_rating(stories):
#     for story in stories:
#         story = calculate_story_rating(story)
#     return stories

# def calculate_story_rating(story):
#     # aggregate the rating in each comment for ALL comments
#     comments = story.comment_set.filter(replied_comment_id=0)
#     story_rating=0
#     for comment in comments:
#         story_rating+=comment.rating
#     story.rating = story_rating
#     return story

# def story_add_tags(tags,story):
#     for tag in tags:
#         name = tag
#         try:
#             tag_object = Tag.objects.get(name=name)
#         except Tag.DoesNotExist:
#             tag_object = Tag.objects.create(name=name)
#         tag_object.stories.add(story)

# def get_all_tags():
#     return Tag.objects.all()