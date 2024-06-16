from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from interactions.tasks import create_like_task, create_subscription_task, create_comment_task


def create_like(request: HttpRequest) -> HttpResponse:
    create_like_task.delay()
    return HttpResponse("TASK STARTED, creating a like")


def create_comment(request: HttpRequest) -> HttpResponse:
    create_comment_task.delay()
    return HttpResponse("TASK STARTED, creating a comment")


def create_subscription(request: HttpRequest) -> HttpResponse:
    create_subscription_task.delay()
    return HttpResponse("TASK STARTED, creating a subscription")
