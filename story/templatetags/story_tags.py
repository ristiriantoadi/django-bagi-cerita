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
            rating_html+="<span class='fa fa-star-half-o checked'></span>"
            rating_counter+=1
        # elif(rating_counter + 2 <= rating):
        else:
            rating_html+="<span class='fa fa-star checked'></span>"
            rating_counter+=2
    return mark_safe(rating_html)

@register.filter(name="render_story_box")
def render_story_box(story):
    story_box_html = f"""<div class="story-box mb-3">
                            <div class="score-box mr-2">
                                <div class="points-number text-center mb-0">{story.rating}</div>
                                <div class="points-text text-center">Points</div>
                            </div>
                            <div class="info">
                                <h5 class="mb-0"><a href="/stories/{story.id}">{story.title}</a></h5>
                                <span class="text-story-info text font-weight-light">(3200 kata) by <a href="/user/{story.user.username}/profile">{story.user.username}</a> on {story.date_posted}</span>
                                <span class="text-story-info text tags font-weight-light">Tags: <a href="twitter.com">Cerita</a> | <a href="twitter.com">Cerita Pendek</a> | <a href="twitter.com">Detektif</a>
                                    | <a href="twitter.com">Cerita</a> | <a href="twitter.com">Cerita Pendek</a> | <a href="twitter.com">Detektif</a> 
                                    | <a href="twitter.com">Cerita</a> | <a href="twitter.com">Cerita Pendek</a> | <a href="twitter.com">Detektif</a>
                                </span>
                            </div>
                        </div>
    """
    return mark_safe(story_box_html)