from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name="render_rating")
def render_rating(rating):
    rating_html = ""
    rating_counter=0
    for x in range(5):
        if(rating_counter>=rating):
           rating_html+="<span class='fa fa-star'></span>"
        elif(rating_counter+2>rating):
            rating_html+="<span class='fas fa-star-half-alt checked'></span>"
            rating_counter+=1
        # elif(rating_counter + 2 <= rating):
        else:
            rating_html+="<span class='fa fa-star checked'></span>"
            rating_counter+=2
    return mark_safe(rating_html)

# @register.filter(name="render_story_box")
# def render_story_box(story):
#     story_box_html = f"""<div class="story-box mb-3">
#                             <div class="score-box mr-2">
#                                 <div class="points-number text-center mb-0">{story.rating}</div>
#                                 <div class="points-text text-center">Points</div>
#                             </div>
#                             <div class="info">
#                                 <h5 class="mb-0"><a href="/stories/{story.id}">{story.title}</a></h5>
#                                 <span class="text-story-info text font-weight-light">(3200 kata) by <a href="/user/{story.user.username}/profile">{story.user.username}</a> on {story.date_posted}</span>
#                                 <span class="text-story-info text tags font-weight-light">Tags: <a href="twitter.com">Cerita</a> | <a href="twitter.com">Cerita Pendek</a> | <a href="twitter.com">Detektif</a>
#                                     | <a href="twitter.com">Cerita</a> | <a href="twitter.com">Cerita Pendek</a> | <a href="twitter.com">Detektif</a> 
#                                     | <a href="twitter.com">Cerita</a> | <a href="twitter.com">Cerita Pendek</a> | <a href="twitter.com">Detektif</a>
#                                 </span>
#                             </div>
#                         </div>
#     """
#     return mark_safe(story_box_html)

@register.inclusion_tag('story/comment.html')
def comment_tag(comment,request):
    return {'comment' : comment,'request':request}

@register.inclusion_tag('story/reply.html')
def reply_tag(comment,request):
    return {'comment' : comment,'request':request}

# render story box
@register.inclusion_tag('story/story_box.html')
def story_box_tag(story):
    return {'story':story}


# @register.filter(name="render_comment")
# def render_comment(comment,args):
#     comment_html= f"""  <div class="comment mb-2">
#                             <h6 class="user font-weight-bold">{comment.user.username}</h6>
#                             <span class="date font-weight-light">(26-08-2020)</span>
#                             <span class="rating">
#                                 { render_rating(comment.rating) }
#                             </span>
#                             <p class="content">{comment.content}</p>
#                             <div class="login-to-comment">
#                   """
#     if(request.user.is_authenticated):
#         comment_html+=f"""<!-- this below is the reply button and the reply box-->
#                             <button onclick="showReplyBox(this)" type="button" data-target="reply-box-{args}" class="btn btn-link">Reply</button>
#                             <form method="POST" class="reply-box" id="reply-box-{args}">
#                                 <div class="form-group no-gutters">
#                                     <textarea class="form-control" name="content" id="exampleFormControlTextarea1" rows="3"></textarea>
#                                 </div>
#                                 <input type="hidden" value="{comment.id}" name="replied_comment_id" >
#                                 <div class="container-button-submit">
#                                     <button type="submit" class="btn btn-primary">Submit</button>
#                                 </div>                
#                             </form>
#                         """
#     else:
#         comment_html+=f"""<button type="button" data-bs-toggle="modal" data-bs-target="#loginModal" class="btn btn-link">Login to reply</button>"""

#     # <div class="login-to-comment">
#     # if(request.user.is_authenticated):
#     #     comment_html+=f"""<!-- this below is the reply button and the reply box-->
#     #                         <button onclick="showReplyBox(this)" type="button" data-target="reply-box-{{forloop.counter}}" class="btn btn-link">Reply</button>
#     #                             <form method="POST" class="reply-box" id="reply-box-{{forloop.counter}}">
#     #                                 <div class="form-group no-gutters">
#     #                                     <textarea class="form-control" name="content" id="exampleFormControlTextarea1" rows="3"></textarea>
#     #                                 </div>
#     #                                 <input type="hidden" value="{{comment.id}}" name="replied_comment_id" >
#     #                                 <div class="container-button-submit">
#     #                                     <button type="submit" class="btn btn-primary">Submit</button>
#     #                                 </div>                
#     #                             </form>
#     #                     """


#     #                                 {"{% if request.user.is_authenticated %}"}
#     #                                     <!-- this below is the reply button and the reply box-->
#     #                                     <button onclick="showReplyBox(this)" type="button" data-target="reply-box-{{forloop.counter}}" class="btn btn-link">Reply</button>
#     #                                     <form method="POST" class="reply-box" id="reply-box-{{forloop.counter}}">
#     #                                         {"{% csrf_token %}"}
#     #                                         <div class="form-group no-gutters">
#     #                                             <textarea class="form-control" name="content" id="exampleFormControlTextarea1" rows="3"></textarea>
#     #                                         </div>
#     #                                         <input type="hidden" value="{{comment.id}}" name="replied_comment_id" >
#     #                                         <div class="container-button-submit">
#     #                                             <button type="submit" class="btn btn-primary">Submit</button>
#     #                                         </div>                
#     #                                     </form>
#     #                                 {"{%else %}"}
#     #                                     <button type="button" data-bs-toggle="modal" data-bs-target="#loginModal" class="btn btn-link">Login to reply</button>
#     #                                 {"{% endif %}"}
#     #                             </div>
#     #                     </div>
#                     # """
#     return mark_safe(comment_html)