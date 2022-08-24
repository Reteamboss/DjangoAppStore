from django import template

register = template.Library()


@register.filter
def view_rating(numb):

    return int(numb) * '\u2605'
