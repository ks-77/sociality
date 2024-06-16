import datetime

from celery import shared_task
from interactions.utils.samples import generate_like, generate_comment, generate_subscription


@shared_task
def create_like_task():
    date = datetime.datetime.now()
    year = date.year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        generate_like()
    else:
        print("it's not a leap year")


@shared_task
def create_comment_task():
    generate_comment()


@shared_task
def create_subscription_task():
    generate_subscription()
