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