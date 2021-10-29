from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from boisubDirectoryApp.models import Authors, Books, FeaturedPerson, BusinessOwners, Businesses
from boisubDirectoryApp.serializer import AuthorsSerializer, BooksSerializer, BusinessesSerializer, BusinessesOwnersSerializer, FeaturedPersonSerializer

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

def home_page(request):

    return render(request, "BlackDatabase.html")


def influencers(request):
    url = 'https://blackindex.herokuapp.com/featuredpersons'
    influencer_data = []

    influencers = requests.get(url).json()

    for influencer in influencers:
        influencer_context = {
            "name": influencer["first_name"],
        }
        influencer_data.append(influencer_context)

    context = {'influencers': influencer_data}
    return render(request, "Influencers.html", context)


@csrf_exempt
def authorsAPI(request, id=0):
    if request.method == 'GET':
        authors = Authors.objects.all()
        authors_serializer = AuthorsSerializer(authors, many=True)
        return JsonResponse(authors_serializer.data, safe=False)
    elif request.method == 'POST':
        authors_data = JSONParser.parse(request)
        authors_serializer = AuthorsSerializer(data=authors_data)

        if authors_serializer.is_valid():
            authors_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        authors_data = JSONParser.parse(request)
        authors = Authors.objects.get(id=authors_data["id"])
        authors_serializer = AuthorsSerializer(authors, data=authors_data)
        if authors_serializer.is_valid():
            authors_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
       authors = Authors.objects.get(id=id)
       authors.delete()
       return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def booksAPI(request, id=0):
    if request.method == 'GET':
        books = Books.objects.all()
        books_serializer = BooksSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    elif request.method == 'POST':
        books_data = JSONParser.parse(request)
        books_serializer = BooksSerializer(data=books_data)
        if books_serializer.is_valid():
           books_serializer.save()
           return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        books_data = JSONParser.parse(request)
        books = Books.objects.get(id=books_data["id"])
        books_serializer = BooksSerializer(books, data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
       books = Books.objects.get(id=id)
       books.delete()
       return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def businessesAPI(request, id=0):
    if request.method == 'GET':
        businesses = Businesses.objects.all()
        businesses_serializer = BusinessesSerializer(businesses, many=True)
        return JsonResponse(businesses_serializer.data, safe=False)
    elif request.method == 'POST':
        businesses_data = JSONParser.parse(request)
        businesses_serializer = BusinessesSerializer(data=businesses_data)
        if businesses_serializer.is_valid():
           businesses_serializer.save()
           return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        businesses_data = JSONParser.parse(request)
        businesses = BusinessesSerializer.objects.get(id=businesses_data["id"])
        businesses_serializer = BusinessesSerializer(
            businesses, data=businesses_data)
        if businesses_serializer.is_valid():
            businesses_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
       businesses = Businesses.objects.get(id=id)
       businesses.delete()
       return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def businessOwnersAPI(request, id=0):
    if request.method == 'GET':
        businessOwners = BusinessOwners.objects.all()
        businessOwners_serializer = BusinessesOwnersSerializer(
            businessOwners, many=True)
        return JsonResponse(businessOwners_serializer.data, safe=False)
    elif request.method == 'POST':
        businessOwners_data = JSONParser.parse(request)
        businessOwners_serializer = BusinessesOwnersSerializer(
            data=businessOwners_data)
        if businessOwners_serializer.is_valid():
           businessOwners_serializer.save()
           return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        businessOwners_data = JSONParser.parse(request)
        businessOwners = BusinessesOwnersSerializer.objects.get(
            id=businessOwners_data["id"])
        businessOwners_serializer = BusinessesOwnersSerializer(
            businessOwners, data=businessOwners_data)
        if businessOwners_serializer.is_valid():
            businessOwners_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
       businessOwners = BusinessOwners.objects.get(id=id)
       businessOwners.delete()
       return JsonResponse("Deleted successfully", safe=False)


@csrf_exempt
def featuredPersonAPI(request, id=0):
    if request.method == 'GET':
        featuredPerson = FeaturedPerson.objects.all()
        featuredPerson_serializer = FeaturedPersonSerializer(
            featuredPerson, many=True)
        return JsonResponse(featuredPerson_serializer.data, safe=False)
    elif request.method == 'POST':
        featuredPerson_data = JSONParser.parse(request)
        featuredPerson_serializer = FeaturedPersonSerializer(
            data=featuredPerson_data)
        if featuredPerson_serializer.is_valid():
           featuredPerson_serializer.save()
           return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        featuredPerson_data = JSONParser.parse(request)
        featuredPerson = FeaturedPersonSerializer.objects.get(
            id=featuredPerson_data["id"])
        featuredPerson_serializer = FeaturedPersonSerializer(
            featuredPerson, data=featuredPerson_data)
        if featuredPerson_serializer.is_valid():
            featuredPerson_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
       featuredPerson = FeaturedPerson.objects.get(id=id)
       featuredPerson.delete()
       return JsonResponse("Deleted successfully", safe=False)
