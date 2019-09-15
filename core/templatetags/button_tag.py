from django import template

register = template.Library()

# Django incluison tag plays elegant way to separete bootstrap template logic
# from app template, that separation is need for theme the projects_type

# Pass in kwargs the elements to fill the cards

# Please note that all templates are contained in cards
# You are free to arrange them in grids or other elements


@register.inclusion_tag('widgets/button.html')
def show_button(*args, **kwargs):
    href = kwargs['href']
    color = ""
    form = ""
    size = ""
    cls_extra = ""
    # Set primary as default bootstrap color class for buttons
    if kwargs.__contains__('color') and kwargs['color'] != "":
        color = "btn-{}".format(kwargs['color'])
    else:
        color = "btn-primary"

    if kwargs.__contains__('form') and kwargs['form'] == "block":
        color = ""

    if kwargs.__contains__('form') and kwargs['form'] == "":
        color = ""

    # The other class are optional
    if kwargs.__contains__('form') and kwargs['form'] != "":
        form = " btn-{}".format(kwargs['form'])
    else:
        form = ""

    if kwargs.__contains__('form') and kwargs['form'] == "icon-split":
        has_span = True
    else:
        has_span = False

    if kwargs.__contains__('size'):
        size = " btn-{}".format(kwargs['size'])
    else:
        size = ""

    if kwargs.__contains__('cls_extra'):
        cls_extra = " {}".format(kwargs['cls_extra'])
    else:
        cls_extra = ""

    btn_classes = "{}{}{}{}".format(color, form, size, cls_extra)

    if kwargs.__contains__('fa_icon'):
        fa_icon = kwargs['fa_icon']
    else:
        fa_icon = False

    if kwargs.__contains__('fa_style'):
        fa_style = kwargs['fa_style']
    else:
        fa_style = False

    caption = kwargs['caption']

    return {'href':href,
            'btn_classes':btn_classes,
            'fa_icon':fa_icon,
            'fa_style':fa_style,
            'caption':caption,
            'has_span':has_span,
            }
