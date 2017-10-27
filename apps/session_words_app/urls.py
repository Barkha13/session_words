from django.conf.urls import url
from . import views           # This line is new!
  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^word_process$',views.word_process),
    url(r'^clear$',views.clear)     # This line has changed!
  ]
