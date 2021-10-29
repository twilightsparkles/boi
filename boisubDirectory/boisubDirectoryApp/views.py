
from django.views.generic import TemplateView

from django.shortcuts import render
import requests


# Create your views here.

# def index(request):
#     url = 'https://blackindex.herokuapp.com/books'
#     book_data = []
#
#     books = requests.get(url).json()
#
#     for book in books:
#         book_context = {
#             "title": book["title"],
#         }
#         book_data.append(book_context)
#
#     context = {'books': book_data}
#     return render(request, "index.html", context)

# def home_page(request):

#     return render(request, "BlackDatabase.html")


# def influencers(request):
#     url = 'https://blackindex.herokuapp.com/featuredpersons'
#     influencer_data = []

#     influencers = requests.get(url).json()

#     for influencer in influencers:
#         influencer_context = {
#             "name": influencer["first_name"],
#         }
#         influencer_data.append(influencer_context)

#     context = {'influencers': influencer_data}
#     return render(request, "Influencers.html", context)


class HomePageView(TemplateView):
    template_name = "BlackDatabase.html"
