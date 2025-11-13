.. :changelog:

History
-------

0.3.0 (2025-11-13)
+++++++++++++++++
Breaking changes

* Dropped support for the following Django versions: 4.0, 4.1, 5.0
* Added support for the following Django versions: 5.1, 5.2

* Dropped support for the following Python versions: 3.8, 3.9
* Added support for the following Python versions: 3.13, 3.14

Minor changes

* Fixed a bug where multiple active_link tags would trigger each other, even when they had different kwargs (like pk).

0.2.2 (2024-07-08)
+++++++++++++++++
Minor changes

* Matches more views
* Code improvements

Important change

* Test coverage dropped to 99.07% from 100%. This is already scheduled to be fixed.

0.2.1 (2024-06-07)
+++++++++++++++++
Important changes

* inactive_class renamed to css_inactive_class.

0.2.0 (2024-06-06)
+++++++++++++++++

* Update build tools to be using Poetry.
* Dropped support for old Django versions, now officially supporting only: Django 4.0, 4.1, 4.2, 5.0.
* Fixed bug where kwargs was not sent to reverse function.

0.1.6 (2019-05-26)
++++++++++++++++++
Important changes

* Silent error when view name not found
* Update test jobs on Travis CI

0.1.5 (2018-05-25)
++++++++++++++++++
* Minor improvements

0.1.4 (2018-04-07)
++++++++++++++++++
* Minor improvements

0.1.3 (2018-02-18)
++++++++++++++++++
* Minor improvements

0.1.2 (2018-01-07)
++++++++++++++++++
* Minor improvements

0.1.1 (2017-10-11)
++++++++++++++++++
* Minor improvements

0.1.0 (2017-07-10)
++++++++++++++++++

* First release on PyPI.
