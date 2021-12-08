from django.urls import path
from ui.views import AuthenticatedHomeView, StudentView, EmployeeView, UnauthorizedView

urlpatterns = [
    path('authenticated/', AuthenticatedHomeView.as_view(), name='authenticated'),
    path('student/', StudentView.as_view(), name='student'),
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('unauthorized/', UnauthorizedView.as_view(), name='unauthorized')
]
