from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements

# I'm using the natural HTML concept of open and close tags just doing it with words
@register.inclusion_tag('cards/approach_card_open.html')
def approach_card_open(*args, **kwargs):
    card_header = kwargs['card_header']

    return {'card_header':card_header,
           }

@register.inclusion_tag('cards/approach_card_close.html')
def approach_card_close():
    return

@register.inclusion_tag('cards/illustration_card.html')
def illustration_card(*args, **kwargs):
    card_header = kwargs['card_header']
    # need the url not the image object
    image_url = kwargs['image_url']
    card_body = kwargs['card_body']

    return {'card_header':card_header,
            'image_url':image_url,
            'card_body':card_body,
           }


@register.inclusion_tag('cards/project_status_card.html')
def project_status_card(*args, **kwargs):
    # project type could be placed in below dictionary but explicit is better
    projects_type = kwargs['projects_type']
    # projects need to be a dictionary of projects
    # been each project a dictionary of project_name and status
    # status a integer [0, 100] the % will be placed as needed, see template
    projects = kwargs['projects']

    return {'projects_type':projects_type,
            'projects':projects,
           }


@register.inclusion_tag('cards/small_card.html')
def small_card(*args, **kwargs):
    # Will be the left side shadow color
    card_color = kwargs['card_color']
    card_title = kwargs['card_title']
    card_value = kwargs['card_value']
    # Fonte Awesome icons for the card
    # Tested fa-calendar fa-dollar-sign fa-clipboard-list fa-comments
    card_faicon = kwargs['card_faicon']

    return {'card_color':card_color,
            'card_title':card_title,
            'card_value':card_value,
            'card_faicon':card_faicon,
           }
