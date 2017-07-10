from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def active_link(context, viewname, css_class='active', strict=False):
    """
    Renders the given CSS class if the request path matches the path of the view.
    :param context: The context where the tag was called. Used to access the request object.
    :param viewname: The name of the view (include namespaces if any).
    :param css_class: The CSS class to render.
    :param strict: If True, the tag will perform an exact match with the request path.
    :return:
    """
    request = context.get('request')
    if request is None:
        # Can't work without the request object.
        return ''
    path = reverse(viewname)
    if strict:
        active = request.path == path
    else:
        active = path in request.path
    if active:
        return css_class
    return ''
