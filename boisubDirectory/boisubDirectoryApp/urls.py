from django.conf.urls import url
from boisubDirectoryApp import views
from django.urls import path

urlpatterns = [
    path('', views.index)
    # url(r'authors/([0-9]+)$', views.authorsAPI ),
    # url(r'^books$', views.booksAPI),
    # url(r'^books/([0-9]+)$', views.booksAPI ),
    # url(r'^businesses$', views.businessesAPI),
    # url(r'^businesses/([0-9]+)$', views.businessesAPI ),
    # url(r'^businessOwners$', views.businessOwnersAPI),
    # url(r'^businessOwners/([0-9]+)$', views.businessOwnersAPI ),
    # url(r'^featuredPersons$', views.featuredPersonAPI),
    # url(r'^featuredPersons/([0-9]+)$', views.featuredPersonAPI ),
]
