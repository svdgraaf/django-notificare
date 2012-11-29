django-notificare

=================
This is a python frontend to the awesome [Notifica.re](https://notifica.re) service.

Installation
============
Django-notificare is easy installable through pip:
```bash
pip install https://github.com/svdgraaf/django-notificare/archive/master.zip
```

Configuration
=============
Django-notificare uses the internal Webhooks from Notifica.re, before you start, create a new [webhook](https://notifica.re/dashboard/services/create/webhook), and give it a fancy name.

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

# send email to given mail address
notificare.email('foo@example.com', short_msg, long_msg)

# call the given number
notificare.call('+3162345678', short_msg, long_text)

# write a reply, and post it the given url
notificare.reply(post_to='http://example.com/', short_msg, long_text)

# open given address in safari
notificare.browse('http://example.com/', short_msg, long_text)

# open the given url, including the schema
notificare.url('chrome://example.com/', short_msg, long_text)


# Ofcourse there is also the send() and callback() command,
# where you have total control over the targets and options:
#
# def send(message, full_message=None, targets=[])
# def callback(url, message=None, full_message=None, keyboard=True)
```

Creating action after comments
==============================
Let's say you have an application, using the [Django comments system](https://docs.djangoproject.com/en/dev/ref/contrib/comments/). After a comments is posted, we want to send a notification: 

```python
from django.db.models.signals import post_save, pre_save
from django.contrib.comments.models import Comment
import django_notificare as notificare

def send_notification(sender, instance, **kwargs)
    if kwargs['created'] == True:
        url = 'http://example.com'  # set your real backend post url here
        notificare.reply(post_to=url, 'Comment posted!', instance.comment)

post_save.connect(send_notification, sender=Comment)
```

Dependencies
============
Django-notificare only depends on [Requests](http://docs.python-requests.org/en/latest/). It doesn't actually need Django to run, just be sure to set the settings correctly in settings.py

Be good to kittens.
