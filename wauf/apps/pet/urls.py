from django.conf.urls import url
from apps.pet.views import index

urlpatterns = [
  url(r'^$', index),
]
