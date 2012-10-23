from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not 'django_proxy_users.auth.backends.LoginAsBackend' in settings.AUTHENTICATION_BACKENDS:
    raise ImproperlyConfigured('django_proxy_users requires the django_proxy_users.auth.backends.LoginAsBackend')

if not 'django_proxy_users.auth.backends.LogBackInAsBackend' in settings.AUTHENTICATION_BACKENDS:
    raise ImproperlyConfigured('django_proxy_users requires the django_proxy_users.auth.backends.LogBackInAsBackend')

if not 'django_proxy_users.contrib.auth.backends.ModelBackend' in settings.AUTHENTICATION_BACKENDS:
    raise ImproperlyConfigured('django_proxy_users requires the django_proxy_users.contrib.auth.backends.ModelBackend')
