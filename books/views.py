from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def index(request):
    return render(request, "index.html")


def books_list(request):
    context = {"books": Book.objects.all()}
    return render(request, "book_list.html", context)


def book_details(request, book_id):
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "book_details.html", context)

