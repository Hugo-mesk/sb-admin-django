from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('example/button.html')
def show_button(*args, **kwargs):
    button = kwargs['btn']
    return {'button':button,}

@register.inclusion_tag('example/button_subgroup.html')
def button_subgroup(*args, **kwargs):

    bt_subgroup = {}
    bt_subgroup['description'] = kwargs['description']
    bt_subgroup['buttons'] = kwargs['buttons']
    return {'bt_subgroup':bt_subgroup,}
