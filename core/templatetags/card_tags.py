from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('blocks/approach_card.html')
def approach_card(*args, **kwargs):
    card_header = kwargs['card_header']
    card_body = kwargs['card_body']

    return {'card_header':card_header,
            'card_body':card_body,
           }


@register.inclusion_tag('blocks/illustration_card.html')
def illustration_card(*args, **kwargs):
    card_header = kwargs['card_header']
    # need the url not the object image
    image_url = kwargs['image_url']
    card_body = kwargs['card_body']

    return {'card_header':card_header,
            'image_url':image_url,
            'card_body':card_body,
           }


@register.inclusion_tag('blocks/project_status_card.html')
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