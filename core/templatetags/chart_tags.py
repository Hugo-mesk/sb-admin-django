from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the charts

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('blocks/chart_area.html')
def chart_area(*args, **kwargs):
    chart_name = kwargs['chart_name']
    chart_menu = kwargs['chart_menu']
    chart = kwargs['chart']

    return {'chart_name':chart_name,
            'chart_menu':chart_menu,
            'chart':chart,
           }
