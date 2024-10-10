from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book_ranking

def main(request):
    return render(request, "main.html") 
   
def writers(request):
    return render(request, "writers.html") 

def hemingway(request):
    return render(request, "hemingway.html")

def shakespeare(request):
    return render(request, "shakespeare.html")

def the_old_man(request):
    return render(request, "the_old_man.html")

def the_sun(request):
    return render(request, "the_sun.html")

def best_books(request):
    books = Book_ranking.objects.all()
    books = books.values()
    context = {
        'books': books,
    }
    return render(request, "books.html", context)

def details(request, id):
    book = Book_ranking.objects.get(id=id)
    context = {
        'book': book,
    }
    return render(request, "details.html", context)

def published_1926(request):
    return render(request, "hem_1926.html")

def published_1940(request):
    return render(request, "hem_1940.html")
    