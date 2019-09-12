from django import template
from django.templatetags.static import static
register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements

@register.inclusion_tag('includes/merge_html.html')
def merge_html(*args, **kwargs):
    html_text = {}
    for html_piece in args:
        html_text.update(html_piece)

    return {"html_text":html_text,
            }
