try:
    from django.conf import settings
except ImportError:
    # We do not need Django perse
    settings = {}

NOTIFICARE_SERVICE_TOKEN = getattr(settings, 'NOTIFICARE_SERVICE_TOKEN', None)
NOTIFICARE_USER_TOKEN = getattr(settings, 'NOTIFICARE_USER_TOKEN', None)
