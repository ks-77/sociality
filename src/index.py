from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, TemplateView


class IndexView(TemplateView):
    template_name = "common/home.html"


# class IndexView(LoginRequiredMixin, DetailView):
#     model = ...
#     form_class = ...
#     template_name = 'common/home.html'
#
#     def get_object(self, queryset=None):
#         user_id = self.kwargs.get("user_id")
#         user_homepage = get_object_or_404(....objects.select_related("user"), user_id=user_id)
#         return user_homepage
