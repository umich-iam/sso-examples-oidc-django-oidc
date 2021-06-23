from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from ui.decorators import student_required, employee_required


class AuthenticatedHomeView(LoginRequiredMixin, TemplateView):

    template_name = "home.html"


@method_decorator(student_required, name='dispatch')
class StudentView(LoginRequiredMixin, TemplateView):

    template_name = "student.html"


@method_decorator(employee_required, name='dispatch')
class EmployeeView(LoginRequiredMixin, TemplateView):

    template_name = "employee.html"


class UnauthorizedView(LoginRequiredMixin, TemplateView):

    template_name = "unauthorized.html"
