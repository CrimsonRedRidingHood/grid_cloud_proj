from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("Welcome");

def genre(request, genre_name):
    qres = Book.objects.filter(genre=genre_name)
    resp = []
    for i in qres:
        resp.append(i.book_name)
        resp.append(i.pub_year)
    return HttpResponse(str(resp))