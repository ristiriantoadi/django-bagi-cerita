from django import template
register = template.Library()
	
@register.filter(name="render_gender")
def render_gender(gender):
    # return rating
    if (gender == "L"):
        return "Laki-laki"
    elif(gender == "P"):
        return "Perempuan"
    else:
        return "-"