==================
Django Active Link
==================

.. image:: https://badge.fury.io/py/django-active-link.svg
    :target: https://badge.fury.io/py/django-active-link

.. image:: https://pyup.io/repos/github/valerymelou/django-active-link/shield.svg
     :target: https://pyup.io/repos/github/valerymelou/django-active-link/
     :alt: Updates

.. image:: https://travis-ci.org/valerymelou/django-active-link.svg?branch=master
    :target: https://travis-ci.org/valerymelou/django-active-link

.. image:: https://codecov.io/gh/valerymelou/django-active-link/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/valerymelou/django-active-link

The simplest way to highlight active links in your Django app.

Documentation
-------------

The full documentation is at https://django-active-link.readthedocs.io.

Quick start
-----------

Install Django Active Link::

    pip install django-active-link

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'active_link',
        ...
    )

To use the ``active_link`` template tag you need to load ``active_link_tags`` templatetags library:

.. code-block:: html

    {% load active_link_tags %}

To add an ``active`` CSS class to a link when the request path matches a given view just do something like this.

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' %}">Menu item</a>

You can even add the active class when the request path matches multiple views. Just pass the view names separated by a double pipe (||) as first argument to the ``active_link`` tag.

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name || view-sub-name' %}">Menu Item</a>

You can also use a custom CSS class:

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' 'custom-class' %}">Menu item</a>

or:

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' css_class='custom-class' %}">Menu item</a>

You can also define an inactive custom css class, that is triggered when a link is deemed not active:

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' 'custom-class' 'not-active' %}">Menu item</a>

or:

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' css_class='custom-class' css_inactive_class='not-active' %}">Menu item</a>

By default ``active_link`` will not perform a strict match. If you want to add the ``active`` class only in case of a strict match pass the ``strict`` argument to the tag:

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link strict=True %}">Menu item</a>

Replace ``view-name`` with the name of your view (including namespaces).

Settings
--------
You can override the default active class and strict mode with the settings ``ACTIVE_LINK_CSS_CLASS``, ``ACTIVE_LINK_CSS_INACTIVE_CLASS`` and ``ACTIVE_LINK_STRICT``.

============================== ==================================================== =============
Key                            Description                                          Default Value
============================== ==================================================== =============
ACTIVE_LINK_CSS_CLASS          Active class to use.                                 `active`
ACTIVE_LINK_CSS_INACTIVE_CLASS Inactive class to use.
ACTIVE_LINK_STRICT             Designates whether to perform a strict match or not. `False`
============================== ==================================================== =============

For more usage examples, please check the full documentation at https://django-active-link.readthedocs.io.

**IMPORTANT**: Django Active Link requires that the current request object is available in your template's context. This means you must be using a `RequestContext` when rendering your template, and `django.template.context_processors.request` must be in your `TEMPLATE_CONTEXT_PROCESSORS` setting. See https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext for more information.

TODO
----

* Write the documentation
* Clean repository for unneccesary files

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install poetry
    (myenv) $ poetry install --only test
    (myenv) $ poetry run tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
