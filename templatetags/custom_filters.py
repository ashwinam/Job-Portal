from django import template

register = template.Library()

def add_class(value, token):
    value.field.widget.attrs['class']=token
    return value

def add_placeholder(value, token):
    value.field.widget.attrs['placement']=token

register.filter(add_class)
register.filter(add_placeholder)