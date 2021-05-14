from django.urls import path
from ui.views import AuthenticatedHomeView

urlpatterns = [
    path('', AuthenticatedHomeView.as_view(), name='authenticated'),
]
