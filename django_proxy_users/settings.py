from django.conf import settings

ORIGINAL_USER_KEY = getattr(settings, 'ORIGINAL_USER_KEY', '_ORIGINAL_USER_KEY')
RECORDS_PER_PAGE = getattr(settings, 'RECORDS_PER_PAGE', 100)
