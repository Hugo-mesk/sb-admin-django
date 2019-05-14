from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the charts

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('blocks/approach_card.html')
def approach_card(*args, **kwargs):
    card_header = kwargs['card_header']
    card_body = kwargs['card_body']

    return {'card_header':card_header,
            'card_body':card_body,
           }
