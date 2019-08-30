"""
Celery configurations

The notification will be issued only once at 8:30
in the morning from Monday to Friday.
"""

import os
import requests

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emeals.settings')
app = Celery('emeals')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'send_menus-please-works': {
        'task': 'emeals.celery.send_menus',
        'schedule': crontab(
            minute=settings.CRONTAB_MINUTE,
            hour=settings.CRONTAB_HOUR,
            day_of_week=settings.CRONTAB_DAY_OF_WEEK
        )
    },
}

app.conf.task_default_queue = 'default'
app.conf.timezone = settings.TIME_ZONE


@app.task(bind=True)
def send_menus(task=None):
    """
    Evaluate if a menu of the day is defined that should be notified
    to the slack channel obtained from the configuration
    """
    from django.conf import settings
    from django.utils import timezone
    from django.urls import reverse
    from menus.models import Menu, MenuDishes

    today = timezone.localtime().strftime('%Y-%m-%d')
    menu_taken = Menu.objects.filter(date=today).exists()

    if menu_taken:
        menu = Menu.objects.get(date=today)
        if menu.is_confirmed:
            menu_dishes = MenuDishes.objects.filter(menu_id=menu.uuid)

            message = '*{}* \n\n'.format(menu.name)

            for menu_dish in menu_dishes:
                message += '- {} *${}*\n'.format(
                    menu_dish.dish.description,
                    menu_dish.dish.price
                )

            path = reverse('menus:menu_of_day', args=(menu.uuid,))

            message += '\n\nTo make your reservation visit following link: {}'.format(
                settings.SITE_DOMINE+path
            )

            session = requests.Session()
            response = session.post(
                settings.SLACK_CHANEL,
                json={
                    "text": message
                }
            )

            print(response.status_code, response.text)
