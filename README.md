django-notificare
=================

This is a python frontend to the awesome Notifica.re service.

Installation
============

Django-notificare is easy installable through pip:
    
    pip install git@github.com:svdgraaf/django-notificare.git

Configuration
=============

Django-notificare uses the internal Webhooks from Notifica.re, before you start, create a new webhook, and give it a fancy name:

https://notifica.re/dashboard/services/create/webhook

Save your tokens in your django settings.py file:

```python
NOTIFICARE_SERVICE_TOKEN = '123'
NOTIFICARE_USER_TOKEN = 'xyz'
```

Usage
=====
Import Django-notificare into your project, and you should be good to go:

```python
import django_notificare as notificare
response = notificare.call('+3162345678', 'short message', 'long message')
print response.json
{u'message': u'aye aye captain!'}
```

Django-notificare implements the several different actions:

```python
import django_notificare as notificare
long_msg = 'longtext is long'
short_msg = 'short msg'  # truncates after 42 chars

notificare.email('foo@example.com', short_msg, long_msg)

notificare.browse('http://example.com/', short_msg, long_text)
notificare.call('+3162345678', short_msg, long_text)
notificare.reply(post_to='http://example.com/', short_msg, long_text)

# Ofcourse there is also the send() and callback() command,
# where you have total control over the targets and options
#
# def send(message, full_message=None, targets=[])
# def callback(url, message=None, full_message=None, keyboard=True)
```

Dependencies
============
django-notificare only depends on Requests. It doesn't actually need django to run, just be sure to set the settings correctly in the 