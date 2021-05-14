from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class AuthenticatedHomeView(LoginRequiredMixin, TemplateView):

    template_name = "home.html"
