from celery import shared_task
from accounts.utils.samples import generate_user


@shared_task
def create_user_task():
    generate_user()
