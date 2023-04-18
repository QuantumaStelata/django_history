from celery import current_app

from history.models import History


@current_app.task(serializer='pickle')
def create_history(*args, **kwargs):
    return History.objects.create(*args, **kwargs)
