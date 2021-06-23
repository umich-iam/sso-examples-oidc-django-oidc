from django.contrib.auth.decorators import user_passes_test


def student_required(function=None):
    """
    Decorator for views that checks that the logged in user is a student,
    redirects to the unauthorized page if not.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_student,
        login_url='/unauthorized',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def employee_required(function=None):
    """
    Decorator for views that checks that the logged in user is an employee,
    redirects to the unauthorized page if not.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_employee,
        login_url='/unauthorized',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
