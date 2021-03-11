from books.models import Book, Author
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, "index.html")


def books_list(request):
    context = {"books": Book.objects.all()}
    return render(request, "books/book_list.html", context)


class BookList(ListView):
    model = Book
    paginate_by = 25
    template_name = "books/book_list.html"
    # context_object_name = "books"


# def author_list(request):
#     context = {"authors": Author.objects.all()}
#     return render(request, "books/author_list.html", context)


class AuthorList(ListView):
    model = Author
    paginate_by = 15
    template_name = "books/author_list.html"


class AuthorDetails(DetailView):
    model = Author
    pk_url_kwarg = "author_id"
    template_name = "books/author_details.html"


def book_details(request, book_id):
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "books/book_details.html", context)


def user_signup(request):
    form = None
    if request.method == "POST":
        # create userdd
        UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/singup_completed.html")
    else:
        # show the empty form
        form = UserCreationForm()
        context = {"form": form}
    return render(request, "registration/signup_form.html", context)


def profile_view(request):
    return render(request, "registration/profile.html")
