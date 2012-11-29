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


# action for opening a url (with schema)
def url(url, message=None, full_message=None, keyboard=False):
    target = {
        'action': 'open web page',
        'url': url,
        'type': 'url',
        'message': keyboard,
    }
    return send(message, full_message, [target])


# callback url, defaults keyboard enabled
def callback(url, message=None, full_message=None, keyboard=True):
    target = {
        'action': 'reply by message',
        'url': url,
        'type': 'callback',
        'message': keyboard,
    }
    return send(message, full_message, [target])


# call the given number
def call(number=None, message=None, full_message=None, keyboard=False):
    return url('mailto:{number}'.format(number=number), message, full_message, keyboard)


# send an action to start a mail to the given address
def email(address, message=None, full_message=None, keyboard=False):
    return url('mailto:{address}'.format(address=address), message, full_message, keyboard)


# open given url in safari
def browse(url, message=None, full_message=None):
    return url('safari://{url}'.format(url=url), message, full_message, False)


# reply to something, and send the details to the given url (enables keyboard)
def reply(post_to, message=None, full_message=None, keyboard=True):
    return callback(post_to, message, full_message, keyboard)
