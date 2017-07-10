=====
Usage
=====

To use Django Active Link in a project, add it to your `INSTALLED_APPS`:

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
