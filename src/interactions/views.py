from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.forms import GenerationQuantityForm
from interactions.tasks import (create_comment_task, create_like_task,
                                create_subscription_task)


def create_like(request: HttpRequest) -> HttpResponse:
    message = None
    if request.method == 'POST':
        form = GenerationQuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            create_like_task.delay(quantity)
            message = "TASK STARTED, creating likes"
    else:
        form = GenerationQuantityForm()
    return render(request, 'generate/general_generation(del).html', {'form': form, 'message': message})


def create_comment(request: HttpRequest) -> HttpResponse:
    message = None
    if request.method == 'POST':
        form = GenerationQuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            create_comment_task.delay(quantity)
            message = "TASK STARTED, creating comments"
    else:
        form = GenerationQuantityForm()
    return render(request, 'generate/general_generation(del).html', {'form': form, 'message': message})


def create_subscription(request: HttpRequest) -> HttpResponse:
    message = None
    if request.method == 'POST':
        form = GenerationQuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            create_subscription_task.delay(quantity)
            message = "TASK STARTED, creating subscriptions"
    else:
        form = GenerationQuantityForm()
    return render(request, 'generate/general_generation(del).html', {'form': form, 'message': message})
