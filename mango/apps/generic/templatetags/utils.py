from django import template


register = template.Library()


@register.filter('klass')
def klass(obj):
    return obj.field.__class__.__name__


@register.filter('widget')
def widget(obj):
    return obj.field.widget.__class__.__name__
