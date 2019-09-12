from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('widgets/button.html')
def show_button(*args, **kwargs):
    url = kwargs['url']
    bootstrap_color = kwargs['bootstrap_color']
    bootstrap_form = kwargs['bootstrap_form']
    bootstrap_size = kwargs['bootstrap_size']
    fa_icon = kwargs['fa_icon']
    caption = kwargs['caption']

    return {'url':url,
            'bootstrap_color':bootstrap_color,
            'bootstrap_form':bootstrap_form,
            'bootstrap_size':bootstrap_size,
            'fa_icon':fa_icon,
            'caption':caption,
            }
