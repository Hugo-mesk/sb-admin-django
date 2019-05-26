from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the charts

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements

# Consider use Plotly or Dash or Bokeh to generate the charts
# or chart.js
@register.inclusion_tag('charts/chart_area.html')
def chart_area(*args, **kwargs):
    chart_name = kwargs['chart_name']
    chart_menu = kwargs['chart_menu']
    chart = kwargs['chart']

    return {'chart_name':chart_name,
            'chart_menu':chart_menu,
            'chart':chart,
           }

# This tag works in conjuction with table css and table js

@register.inclusion_tag('table/table.html')
def table_area(*args, **kwargs):
    table_heads = kwargs['table_heads']
    table_data = kwargs['table_data']
    if kwargs.__contains__('has_foot'):
        has_foot = kwargs['has_foot']
    else:
        has_foot = false

    # The table foot defaults to be a copy of header
    # In any case that make sence to you provide a table_foot
    if kwargs.__contains__('table_foot'):
        table_foot = kwargs['table_foot']
    else:
        table_foot = kwargs['table_heads']

    return {'table_heads':table_heads,
            'table_data':table_data,
            'has_foot':has_foot,
            'table_foot':table_foot,
           }

@register.inclusion_tag('table/table_css.html')
def table_css(*args, **kwargs):
    return {
            'table_css':True,
    }

@register.inclusion_tag('table/table_js.html')
def table_js(*args, **kwargs):
    return {
            'table_js':True,
    }
