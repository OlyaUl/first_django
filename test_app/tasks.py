# Create your tasks here
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import shared_task
# from celery. decorators import periodic_task

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_test.settings")

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# @app.task(bind=True)
@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


'''def books(request):
    # return HttpResponse("Hello, world!")
    books = Book.objects.all()
    return render(request, 'test_app/books.html',
                  {'books': books})'''


@shared_task
def add(x, y):
    print(x+y)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
