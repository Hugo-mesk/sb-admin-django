from django import template
from django.templatetags.static import static
register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements

@register.inclusion_tag('includes/messages.html')
def message_dropdown(*args, **kwargs):
    # The pop method of dictionary search, return and remove the key values
    # and also accepts a default value if key is not found
    # This is only for test
    messages = {}
    print(args)
    for message in args:
        messages.update(message)

    return {"messages":messages,}


@register.simple_tag()
def set_message(*args, **kwargs):
    # Set link receiver link name, url and fa icon from below options
    # fa-user, fa-list, fa-cogs

    message = {}
    name =  kwargs['sender']
    message['sender'] = kwargs['sender']
    message['bg'] = kwargs['bg']
    message['was_read'] =  kwargs['was_read']
    message['time_lapse'] = kwargs['time_lapse']
    message['short_text'] = kwargs['short_text']
    if kwargs.__contains__('sender_img'):
        message['sender_img'] =static(kwargs['sender_img'])
    else:
        message['sender_img'] = static("/img/no_img.jpeg")

    return {name:message}
