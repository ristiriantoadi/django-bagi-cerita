from story.models import Story,Comment,Tag
from django.core.paginator import Paginator
from django.http import Http404

def get_points(user):
    return len(Comment.objects.filter(user=user,replied_comment_id=0))*5

def get_stories(user=None,category="all",search=None):

    # search = {"search_by":"tag","key":"something"} or {"search_by":"judul","key":"something"}

    if(user):
        stories = Story.objects.filter(user=user)
    else:
        stories = Story.objects.all()
        
    returned_stories=[]
    for story in stories:
        story = get_story(story)

        # filter stories by tag or judul
        if(search):
            if(search["search_by"] == "tag"):
                if len(story.tag_set.filter(name=search["key"])) != 0:
                    returned_stories.append(story)
            else:
                # if story.title == search["key"]
                if search["key"].lower() in story.title.lower():
                    returned_stories.append(story)
        else:        
            # filter stories by category
            if(category == "all"):
                returned_stories.append(story)
            elif(category == "popular"):
                if(story.rating >= 35 and story.rating <=50):
                    returned_stories.append(story)
            elif(category=="best"):
                if(story.rating >= 51 and story.rating <=100):
                    returned_stories.append(story)
            else:
                if(story.rating>100):
                    returned_stories.append(story)
    return returned_stories

def get_story(story):
    # get the tags and the rating
    story.tags = story.tag_set.all()
    story.date_posted = story.date_posted.strftime("%B %d %Y")
    story = calculate_story_rating(story)
    return story

# get notifications
# status is either 'unread' or 'all'
def get_comments_notification(user,status):
    if(status == "unread"):
	    comments = Comment.objects.filter(read_status=False,replied_comment_id=0)
    else:
	    comments = Comment.objects.filter(replied_comment_id=0)

    comments_notif = []
    for comment in comments:
        if(comment.story.user == user):
            comments_notif.append(comment)
            if(status != "unread"):
                comment.read_status = True
                comment.save()

    return comments_notif


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

def count_words(content):
    words_count=0
    if content != '':
        # splitting the text and taking lenght
        # of that
        words_count = len(content.split())    
    return words_count

def story_add_tags(tags,story):
    for tag in tags:
        name = tag
        try:
            tag_object = Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            tag_object = Tag.objects.create(name=name)
        tag_object.stories.add(story)

def get_all_tags():
    return Tag.objects.all()

def pagination(stories,request):
    paginator = Paginator(stories, 5)
    page=1
    if(request.GET.get("page")):
        page = request.GET.get("page")
    stories = paginator.get_page(page)
    stories.len = len(stories)
    return stories

def is_authorized_to_update_story(story_id,request):
    try:
        story = Story.objects.get(id=story_id)
    except Story.DoesNotExist:
        raise Http404("Story does not exist")
    if(str(story.user) != str(request.user)):
        return False
    return True