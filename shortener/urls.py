from django.urls import path, re_path

from .views import LinkCreateView, shortened_link_redirect_view

urlpatterns = [
    path('', LinkCreateView.as_view(), name='home'),    
    re_path(r'^s/(?P<short_link>\w+)$', LinkCreateView.as_view(), name="return_shortened_link"),
    re_path(r'^(?P<short_link>\w+)$', shortened_link_redirect_view, name="redirect_view")
]
