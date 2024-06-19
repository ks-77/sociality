from celery import shared_task

from blog.utils.samples import generate_post, generate_story


@shared_task
def create_story_task():
    generate_story()


@shared_task
def create_post_task():
    generate_post()
