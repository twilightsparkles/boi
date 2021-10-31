from django.conf.urls import url
from boisubDirectoryApp import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^influencers/$', views.Influencers.as_view(), name='influencers'),
    url(r'^$', views.BooksView.as_view(), name='books'),
    url(r'^$', views.AuthorsView.as_view(), name='authors'),
    url(r'^$', views.BeautyView.as_view(), name='beauty'),
    url(r'^$', views.FashionView.as_view(), name='fashion'),
    url(r'^$', views.HealthView.as_view(), name='health'),
    url(r'^$', views.HomeView.as_view(), name='homedecor'),
    url(r'^$', views.ServiceView.as_view(), name='services'),
    url(r'^$', views.FoodView.as_view(), name='food'),
    url(r'^$', views.BusinessOwnersView.as_view(), name='businessowners'),
    url(r'^business$', views.BusinessView.as_view(), name='business'),
    path('featuredpersons/', views.influencers),
    path('books/', views.books),
    path('authors/', views.authors),
    path('businesses/beauty', views.beauty),
    path('businesses/fashion', views.fashion),
    path('businesses/health', views.health),
    path('businesses/homedecor', views.homeDecor),
    path('businesses/services', views.services),
    path('businesses/food', views.food),
    path('businessowners', views.businessOwners)
    ]
