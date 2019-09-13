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


@register.inclusion_tag('cards/small_card.html')
def small_card(*args, **kwargs):
    # Will be the left side shadow color
    bootstrap_color = kwargs['bootstrap_color']
    title = kwargs['title']
    value = kwargs['value']
    # Fonte Awesome icons for the card
    # Tested fa-calendar fa-dollar-sign fa-clipboard-list fa-comments
    fa_icon = kwargs['fa_icon']

    return {'bootstrap_color':bootstrap_color,
            'title':title,
            'value':value,
            'fa_icon':fa_icon,
           }
