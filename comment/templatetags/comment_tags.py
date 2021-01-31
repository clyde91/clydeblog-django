from django import template

register = template.Library()  # 注意L大写

@register.simple_tag
def test():
    return "test code"
