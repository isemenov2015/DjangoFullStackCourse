from django import template

register = template.Library()

def cut_str(value, arg):
    """
    Cuts all values of ARG from the string VALUE
    """
    return value.replace(arg, "")

register.filter('cut_str', cut_str)

#Alternative way of filter register with Decorator

@register.filter(name='cut_dots')
def cut_str2(value, arg):
    """
    Replaces all values of arg with '...'
    """
    return value.replace(arg, "...")
