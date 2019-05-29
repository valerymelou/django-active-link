=====
Usage
=====

To use Django Active Link in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'active_link',
        ...
    )

**IMPORTANT**: Django Active Link requires that the current request object is available in your template's context. This means you must be using a `RequestContext` when rendering your template, and `django.core.context_processors.request` must be in your `TEMPLATE_CONTEXT_PROCESSORS` setting. See [the documentation](https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext) for more information.

To use the `active_link` template tag you need to load `active_link_tags` templatetags library:

    {% load active_link_tags %}

To add an `active` CSS class to a link when the request path matches a given view just do something like this.

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' %}">Menu item</a>

You can even add the active class when the request path matches multiple views. Just pass the view names separated by a pipe (||) as first argument to the ``active_link`` tag.

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name || view-sub-name' %}">Menu Item</a>

You can also match views that take arguments. For example:

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name-with-args' pk=12 slug='simple-slug' %}">Menu item</a>

Replace `view-name` with the name of your view (including namespaces).
