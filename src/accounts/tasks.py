from celery import shared_task

from accounts.utils.samples import generate_user


@shared_task
def create_user_task(quantity):
    for _ in range(quantity):
        generate_user()
