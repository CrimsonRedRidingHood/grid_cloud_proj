from django.shortcuts import render

from django.http import HttpResponse

from .models import Book

# Create your views here.

def index(request):
    static_file = open('index.html', 'r')
    contents = static_file.read()
    static_file.close()
    return HttpResponse(contents);

def genre(request, genre_name):
    qres = Book.objects.filter(genre=genre_name)
    resp = []
    for i in qres:
        resp.append(i.book_name)
        resp.append(i.pub_year)
    stringified = str(resp)
    stringified.replace("'", '"') # =D
    return HttpResponse(stringified)