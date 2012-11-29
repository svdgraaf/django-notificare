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

    NOTIFICARE_SERVICE_TOKEN = '123'
    NOTIFICARE_USER_TOKEN = 'xyz'

Usage
=====
Import Django-notificare into your project, and you should be good to go:

    import django_notificare as notificare
    response = notificare.call('+3162345678', 'short message', 'long message')
    print response.json
    {u'message': u'aye aye captain!'}

Django-notificare implements the several different actions:

    import django_notificare as notificare
    notificare.email('foo@example.com', 'foobar', 'foobarred')
    notificare.url('http://svdgraaf.nl/', 'foobar', 'foobarred')
    notificare.call('+3162345678', 'short message', 'long message')
    notificare.reply('http://example.com/', 'foobar', 'foobarrrrrred', keyboard=True)  # keyboard optional
    # Ofcourse there is also the custom send() command, where you have total
    # control over the targets
    notificare.send('foobar', full_message='foobarrrred', targets=[]):


Dependencies
============
django-notificare only depends on Requests. It doesn't actually need django to run, just be sure to set the settings correctly in the 