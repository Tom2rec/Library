from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


def index(request):
    return render(request, "test.html")


def books_list(request):
    contex = {"books": Book.objects.all()}
    return render(request, "book_list.html", contex);
