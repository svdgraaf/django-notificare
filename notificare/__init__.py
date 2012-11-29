from django_notificare import settings
import requests


def send(message, full_message=None, targets=[]):
    service_token = settings.NOTIFICARE_SERVICE_TOKEN
    user_token = settings.NOTIFICARE_USER_TOKEN

    url = 'https://apps.notifica.re/hooks/webhook/{service}?token={user}'.format(service=service_token, user=user_token)
    data = {
        'message': message,
        'fullMessage': full_message,
        'targets': targets
    }
    r = requests.post(url, data)
    return r


def call(number=None, message=None, full_message=None, keyboard=False):
    target = {
        'action': 'call',
        'url': 'tel://' + str(number),
        'type': 'url',
        'message': keyboard,
    }
    return send(message, full_message, [target])


def email(address, message=None, full_message=None, keyboard=False):
    target = {
        'action': 'reply by email',
        'url': 'mailto:{address}'.format(address),
        'type': 'url',
        'message': keyboard,
    }
    return send(message, full_message, [target])


def url(url, message=None, full_message=None):
    target = {
        'action': 'open web page',
        'url': 'safari://{url}'.format(url),
        'type': 'url',
        'message': False,
    }
    return send(message, full_message, [target])


def reply(url, message=None, full_message=None, keyboard=True):
    target = {
        'action': 'reply by message',
        'url': url,
        'type': 'callback',
        'message': keyboard,
    }
    return send(message, full_message, [target])


def callback(url, message=None, full_message=None):
    target = {
        'action': 'open web page',
        'url': 'safari://{url}'.format(url),
        'type': 'url',
        'message': False,
    }
    return send(message, full_message, [target])
