from django.contrib.auth import models as DjangoAuthModels
from django_proxy_users import settings as ProxyUsersSettings

ORIGINAL_USER_KEY = ProxyUsersSettings.ORIGINAL_USER_KEY


def login_as(request):
    data = {}
    user_id = request.session.get(ORIGINAL_USER_KEY, False)
    if request.user.is_authenticated:
            try:
                data = {
                    ORIGINAL_USER_KEY: DjangoAuthModels.User.objects.get(pk=user_id),
                }
            except DjangoAuthModels.User.DoesNotExist:
                pass
    return data
