
About this package
==================

Required components.
--------------------

Within the application we have integral components that are necessary
to run this app.

* Forms
    * django_proxy_users.forms.AuthenticationForm (extends django.contrib.auth.forms.AuthenticationForm, django.core.paginator.Paginator)
    * django_proxy_users.forms.AuthenticateAsForm (extends django.contrib.auth.forms.Form)

* Backends
    * django_proxy_users.auth.backends.LoginAsBackend
    * django_proxy_users.auth.backends.LogBackInAsBackend

* Context Processors
    * django_proxy_users.context_processors.login_as


Sample Components and Open Source Libraries.
--------------------------------------------

* Open Source Libraries
    * Jquery 1.8.2
    * Twitter Bootstrap
* Views
    * django_proxy_users.views.home
    * django_proxy_users.views.login
    * django_proxy_users.views.login
    * django_proxy_users.views.logout
    * django_proxy_users.views.login_as
    * django_proxy_users.views.log_back_in_as

Install & Configure
===================

Required Steps to get it working.
----------------------------

1. Get the code source from either:
    * Download and place within your django app.
        * http://pypi.python.org/pypi/django-proxy-user/
        * https://github.com/jturo/django-proxy-users
    * OR PIP install
        * pip install django-proxy-users

2. Install the app in setttings.py.::

    INSTALLED_APPS = (
        ...
        'django_proxy_users',
        ...
    )

3. Add context processors.::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django_proxy_users.context_processors.login_as',
        ...
    )

4. Add Authentication Backends.::

    AUTHENTICATION_BACKENDS = (
        ...
        "account.auth.backends.LoginAsBackend",
        "account.auth.backends.LogBackInAsBackend",
        "django.contrib.auth.backends.ModelBackend",
        ...
    )

Additional and Optional Configuration Options (settings.py).
-------------------------------------------------------------

**ORIGINAL_USER_KEY**  session key where the original user is stored