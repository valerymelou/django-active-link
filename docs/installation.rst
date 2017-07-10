============
Installation
============

At the command line::

    $ easy_install django-active-link

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv django-active-link
    $ pip install django-active-link

Add `active_link` to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'active_link',
        ...
    )

That's it. You can start using Django Active Link in your templates.
