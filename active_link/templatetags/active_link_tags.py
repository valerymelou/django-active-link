from django import template
from django.conf import settings
from django.urls import NoReverseMatch, reverse
from django.utils.encoding import escape_uri_path

register = template.Library()


@register.simple_tag(takes_context=True)
def active_link(
    context, viewnames, css_class=None, inactive_class="", strict=None, *args, **kwargs
):
    """
    Renders the given CSS class if the request path matches the path of the view.
    :param context: The context where the tag was called. Used to access the request object.
    :param viewnames: The name of the view or views separated by || (include namespaces if any).
    :param css_class: The CSS class to render.
    :param inactive_class: The CSS class to render if the views is not active.
    :param strict: If True, the tag will perform an exact match with the request path.
    :return:
    """
    if css_class is None:
        css_class = getattr(settings, "ACTIVE_LINK_CSS_CLASS", "active")

    if strict is None:
        strict = getattr(settings, "ACTIVE_LINK_STRICT", False)

    request = context.get("request")
    if request is None:
        # Can't work without the request object.
        return inactive_class

    if request.resolver_match is not None:
        # Capture the url kwargs to reverse against
        request_kwargs = request.resolver_match.kwargs
        kwargs.update(request_kwargs)

    active = False
    views = viewnames.split("||")

    for viewname in views:
        try:
            path = reverse(viewname.strip(), args=args, kwargs=kwargs)
        except NoReverseMatch:
            continue
        request_path = escape_uri_path(request.path)
        if strict:
            active = request_path == path
        else:
            active = request_path.find(path) == 0
        if active:
            break

    if active:
        return css_class

    return inactive_class
