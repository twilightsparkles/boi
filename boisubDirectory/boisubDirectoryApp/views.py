
from django.views.generic import TemplateView
from django.shortcuts import render
import requests


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

def beauty(request):
    url = 'https://blackindex.herokuapp.com/businesses?tag=eq.BEAUTY'
    data = []

    models = requests.get(url).json()

    for model in models:
        model_context = {
            "name" : model["name"],
            "description": model["description"],
            "image_url": model["image_url"],
            "website_link": model["website_link"]
        }
        data.append(model_context)

    context = {'businesses': data}
    return render(request, "beauty.html", context)

def fashion(request):
    url = 'https://blackindex.herokuapp.com/businesses?tag=eq.FASHION'
    data = []

    models = requests.get(url).json()

    for model in models:
        model_context = {
            "name" : model["name"],
            "description": model["description"],
            "image_url": model["image_url"],
            "website_link": model["website_link"]
        }
        data.append(model_context)

    context = {'businesses': data}
    return render(request, "fashion.html", context)

def health(request):
    url = 'https://blackindex.herokuapp.com/businesses?tag=eq.HEALTH%20AND%20WELLNESS'
    data = []

    models = requests.get(url).json()

    for model in models:
        model_context = {
            "name": model["name"],
            "description": model["description"],
            "image_url": model["image_url"],
            "website_link": model["website_link"]
        }
        data.append(model_context)

    context = {'businesses': data}
    return render(request, "health.html", context)


def food(request):
    url = 'https://blackindex.herokuapp.com/businesses?tag=eq.FOOD%20AND%20DRINK'
    data = []

    models = requests.get(url).json()

    for model in models:
        model_context = {
            "name": model["name"],
            "description": model["description"],
            "image_url": model["image_url"],
            "website_link": model["website_link"]
        }
        data.append(model_context)

    context = {'businesses': data}
    return render(request, "health.html", context)

def homeDecor(request):
    url = 'https://blackindex.herokuapp.com/businesses?tag=eq.HOME%20DECOR%20AND%20GIFTS'
    data = []

    models = requests.get(url).json()

    for model in models:
        model_context = {
            "name": model["name"],
            "description": model["description"],
            "image_url": model["image_url"],
            "website_link": model["website_link"]
        }
        data.append(model_context)

    context = {'businesses': data}
    return render(request, "home.html", context)



def services(request):
    url = 'https://blackindex.herokuapp.com/businesses?tag=eq.SERVICES'
    data = []

    models = requests.get(url).json()

    for model in models:
        model_context = {
            "name": model["name"],
            "description": model["description"],
            "image_url": model["image_url"],
            "website_link": model["website_link"]
        }
        data.append(model_context)

    context = {'businesses': data}
    return render(request, "services.html", context)

class HomePageView(TemplateView):
    template_name = "BlackDatabase.html"

class Influencers(TemplateView):
    template_name = "Influencers.html"

class BooksView(TemplateView):
    template_name = "books.html"

class AuthorsView(TemplateView):
    template_name = "authors.html"

class BusinessView(TemplateView):
    template_name = "business.html"

class BeautyView(TemplateView):
    template_name = "beauty.html"

class FashionView(TemplateView):
    template_name = "fashion.html"

class HealthView(TemplateView):
    template_name = "health.html"

class HomeView(TemplateView):
    template_name = "home.html"

class ServiceView(TemplateView):
    template_name = "services.html"

class FoodView(TemplateView):
    template_name = "food.html"