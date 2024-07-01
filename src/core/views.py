from django.shortcuts import render
from django.views.generic import TemplateView


def custom_404_view(request, exception):
    return render(request, "errors/error-404.html", status=404)


class ComingSoonView(TemplateView):
    template_name = "errors/coming-soon.html"
