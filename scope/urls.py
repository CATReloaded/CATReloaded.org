from django.conf.urls import url, include

from .views import ScopeIndex


urlpatterns = [
    url(r'^', ScopeIndex.as_view(), name='index'),
]
