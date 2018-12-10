from django import template

register = template.Library()


@register.filter(is_safe=True)
def highlight(value, arg):
    value = value.replace(arg, '<span style="background-color: #40B67B;">{arg}</span>'.format(arg=arg))
    value = value.replace(arg.capitalize(), '<span style="background-color: #40B67B;">{arg}</span>'.format(arg=arg.capitalize()))
    value = value.replace(arg.upper(), '<span style="background-color: #40B67B;">{arg}</span>'.format(arg=arg.upper()))
    return value

