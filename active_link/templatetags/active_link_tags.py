from django import template
from django.conf import settings
from django.urls import NoReverseMatch, reverse
from django.utils.encoding import escape_uri_path

register = template.Library()


@register.simple_tag(takes_context=True)
def active_link(
    context,
    viewnames,
    css_class=None,
    css_inactive_class="",
    strict=None,
    *args,
    **kwargs
):
    """
    Renders the given CSS class if the request path matches the path of the view.
    :param context: The context where the tag was called. Used to access the request object.
    :param viewnames: The name of the view or views separated by || (include namespaces if any).
    :param css_class: The CSS class to render if the view is active.
    :param css_inactive_class: The CSS class to render if the view is not active.
    :param strict: If True, the tag will perform an exact match with the request path.
    :return:
    """
    if css_class is None:
        css_class = getattr(settings, "ACTIVE_LINK_CSS_CLASS", "active")

    if css_inactive_class == "":
        css_inactive_class = getattr(settings, "ACTIVE_LINK_CSS_INACTIVE_CLASS", "")

    if strict is None:
        strict = getattr(settings, "ACTIVE_LINK_STRICT", False)

    request = context.get("request")
    if request is None:
        # Can't work without the request object.
        return css_inactive_class

    resolver_kwargs = {}
    if hasattr(request, "resolver_match") and hasattr(request.resolver_match, "kwargs"):
        resolver_kwargs = request.resolver_match.kwargs

    kwargs.update(resolver_kwargs)

    active = False
    views = viewnames.split("||")
    request_path = escape_uri_path(request.path)

    for viewname in views:
        try:
            path = reverse(viewname.strip(), args=args, kwargs=kwargs)
        except NoReverseMatch:
            continue

        if strict:
            active = request_path == path
        else:
            active = request_path.startswith(path) or path.startswith(request_path)
        if active:
            break

    if active:
        return css_class

    return css_inactive_class
