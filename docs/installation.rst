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

Make sure `django.template.context_processors.request` is added in your template context_processors:

.. code-block:: python

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": (os.path.join(BASE_DIR, "templates"),),
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                    # list if you haven't customized them:
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.request",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                ],
                "debug": True,
            },
        },
    ]

That's it. You can start using Django Active Link in your templates.
