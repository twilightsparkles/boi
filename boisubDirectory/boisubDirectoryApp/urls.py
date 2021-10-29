from django.conf.urls import url
from boisubDirectoryApp import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^influencers/$', views.Influencers.as_view(), name='influencers'),
    path('featuredpersons/', views.influencers)
]
