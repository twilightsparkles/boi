
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



def influencers(request):
    url = 'https://blackindex.herokuapp.com/featuredpersons'
    influencer_data = []

    influencers = requests.get(url).json()

    for influencer in influencers:
        influencer_context = {
            "name": influencer["first_name"],
            "website_link": influencer["website_link"]
        }
        influencer_data.append(influencer_context)

    context = {'influencers': influencer_data}
    return render(request, "Influencers.html", context)

def books(request):
    url = 'https://blackindex.herokuapp.com/books'
    book_data = []

    books = requests.get(url).json()

    for book in books:
        book_context = {
            "image_url": book["image_url"],
            "author_name" : book["author_name"],
            "title": book["title"],
            "book_description": book["description"]
        }
        book_data.append(book_context)

    context = {'books': book_data}
    return render(request, "books.html", context)

def authors(request):
    url = 'https://blackindex.herokuapp.com/authors'
    authors_data = []

    authors = requests.get(url).json()

    for author in authors:
        author_context = {
            "name" : author["author_first_name"] + author["author_last_name"],
            "image_url": author["image_url"],
            "bio": author["biography"]
        }
        authors_data.append(author_context)

    context = {'authors': authors_data}
    return render(request, "authors.html", context)

class HomePageView(TemplateView):
    template_name = "BlackDatabase.html"

class Influencers(TemplateView):
    template_name = "Influencers.html"

class BooksView(TemplateView):
    template_name = "books.html"

class AuthorsView(TemplateView):
    template_name = "authors.html"