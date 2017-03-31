from django.conf.urls import url
from apps.adoption.views import index

urlpatterns = [
  url(r'^$', index),
]
