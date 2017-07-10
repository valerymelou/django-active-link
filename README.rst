=============================
Django Active Link
=============================

.. image:: https://badge.fury.io/py/django-active-link.svg
    :target: https://badge.fury.io/py/django-active-link

.. image:: https://travis-ci.org/valerymelou/django-active-link.svg?branch=master
    :target: https://travis-ci.org/valerymelou/django-active-link

.. image:: https://codecov.io/gh/valerymelou/django-active-link/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/valerymelou/django-active-link

The best way to highlight active links in your Django app.

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
        'active_link.apps.ActiveLinkConfig',
        ...
    )

Add Django Active Link's URL patterns:

.. code-block:: python

    from active_link import urls as active_link_urls


    urlpatterns = [
        ...
        url(r'^', include(active_link_urls)),
        ...
    ]

Features
--------

* TODO

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
