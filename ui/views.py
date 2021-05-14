from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class AuthenticatedView(LoginRequiredMixin, TemplateView):

    template_name = "authenticated.html"
