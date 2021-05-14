from django.urls import path
from ui.views import AuthenticatedView

urlpatterns = [
    path('authenticated', AuthenticatedView.as_view(), name='authenticated'),
]
