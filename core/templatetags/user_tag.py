from django import template
register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements

@register.inclusion_tag('includes/user_info.html')
def user_dropdown(*args, **kwargs):
    # The pop method of dictionary search, return and remove the key values
    # and also accepts a default value if key is not found
    user_img = kwargs.pop("user_img","/static/img/user_default.jpeg")
    # This is only for test
    user_links = {}
    print(args)
    for link in args:
        user_links.update(link)

    return {"user_links":user_links,
            "user_img":user_img,}


@register.simple_tag()
def set_link(*args, **kwargs):
    # Set link receiver link name, url and fa icon from below options
    # fa-user, fa-list, fa-cogs

    link = {}
    name =  kwargs['link']
    link['url'] = kwargs['url']
    link['icon'] = kwargs['icon']

    return {name:link}
