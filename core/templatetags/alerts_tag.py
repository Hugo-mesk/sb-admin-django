from django import template
from django.templatetags.static import static
from datetime import datetime
register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements

@register.inclusion_tag('includes/alerts.html')
def alerts_dropdown(*args, **kwargs):
    # Obs: this code does not handle date time format or timezone
    # this shoud be handled in your's views
    alerts = {}
    print(args)
    for alert in args:
        alerts.update(alert)

    return {"alerts":alerts,}


@register.simple_tag()
def set_alert(*args, **kwargs):
    # Set alert number, badge, read, date, text, fa icon from below options
    # fa-file-alt, fa-donate, fa-exclamation-triangle
    # Obs: this code does not handle date time format or timezone
    # this shoud be handled in your's views

    alert = {}
    number =  kwargs['number']
    alert['bg'] = kwargs['bg']
    alert['was_read'] =  kwargs['was_read']
    alert['date'] = kwargs['date']
    alert['short_text'] = kwargs['short_text']
    alert['fa_icon'] = kwargs['fa_icon']


    return {number:alert}
