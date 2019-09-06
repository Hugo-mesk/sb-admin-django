from django import template
register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('includes/sidebar.html')
def sidebar(*args, **kwargs):
    # Site name and version in kwargs as you may supply them
    # or get from a site app
    site_name = kwargs['site_name']
    site_version = kwargs['site_version']

    return {'site_name':site_name,
            'site_version':site_version,
            #'pages':pages,
           }
