from django import template

register = template.Library()

@register.inclusion_tag('blocks/approach_card.html')
def approach_card(*args, **kwargs):
    card_header = kwargs['card_header']
    card_body = kwargs['card_body']

    return {'card_header':card_header,
            'card_body':card_body,
           }


@register.inclusion_tag('blocks/illustration_card.html')
def illustration_card(*args, **kwargs):
    card_header = kwargs['card_header']
    image_url = kwargs['image_url']
    card_body = kwargs['card_body']

    return {'card_header':card_header,
            'image_url':image_url,
            'card_body':card_body,
           }
