from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^team/$', views.TeamPageView.as_view()),
]
