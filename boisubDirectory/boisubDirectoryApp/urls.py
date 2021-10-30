from django.conf.urls import url
from boisubDirectoryApp import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^influencers/$', views.Influencers.as_view(), name='influencers'),
    url(r'^$', views.BooksView.as_view(), name='books'),
    url(r'^$', views.AuthorsView.as_view(), name='authors'),
    path('featuredpersons/', views.influencers),
    path('books/', views.books),
    path('authors/', views.authors)
]
