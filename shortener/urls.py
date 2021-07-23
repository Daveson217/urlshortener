from django.urls import path, re_path

from .views import LinkCreateView

urlpatterns = [
    path('', LinkCreateView.as_view(), name='home'),
    re_path(r'^(?P<shortened_link>\w+)$', LinkCreateView.as_view(), name="return_shortened_link"),
]
