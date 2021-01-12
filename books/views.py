from books.models import Book
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, "index.html")


def books_list(request):
    context = {"books": Book.objects.all()}
    return render(request, "book_list.html", context)


def book_details(request, book_id):
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "book_details.html", context)


def user_signup(request):
    form = None
    if request.method == "POST":
        # create userdd
        UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/singup_completed.html")
    else:
        #show the empty form
        form = UserCreationForm()
        context = {"form":form}
    return render(request, "registration/signup_form.html", context)
