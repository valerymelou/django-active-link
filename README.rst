==================
Django Active Link
==================

.. image:: https://badge.fury.io/py/django-active-link.svg
    :target: https://badge.fury.io/py/django-active-link

.. image:: https://travis-ci.org/valerymelou/django-active-link.svg?branch=master
    :target: https://travis-ci.org/valerymelou/django-active-link

.. image:: https://codecov.io/gh/valerymelou/django-active-link/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/valerymelou/django-active-link

The simplest way to highlight active links in your Django app.

Documentation
-------------

The full documentation is at https://django-active-link.readthedocs.io.

Quickstart
----------

Install Django Active Link::

    pip install django-active-link

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'active_link',
        ...
    )

**IMPORTANT**: Django Active Link requires that the current request object is available in your template's context. This means you must be using a `RequestContext` when rendering your template, and `django.core.context_processors.request` must be in your `TEMPLATE_CONTEXT_PROCESSORS` setting. See https://docs.djangoproject.com/en/dev/ref/templates/api/#subclassing-context-requestcontext for more information.

To use the `active_link` template tag you need to load `active_link_tags` templatetags library:

.. code-block:: html

    {% load active_link_tags %}

To add an `active` CSS class to a link when the request path matches a given view just do something like this.

.. code-block:: html

    <a href="{% url 'view-name' %}" class="{% active_link 'view-name' %}">Menu item</a>

Replace `view-name` with the name of your view (including namespaces).

For more usage examples, please check the full documentation at https://django-active-link.readthedocs.io.

TODO
----

* Accept URLs args in `active_link` tag
* Write the documentation

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
