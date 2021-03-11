"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from books.views import book_details, index, user_signup, profile_view, BookList, AuthorDetails, AuthorList
urlpatterns = [
    path('', index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', user_signup),
    path('accounts/profile/', profile_view, name="user_profile"),
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name="book_list"),
    path('authors/', AuthorList.as_view(), name="author_list"),
    path("authors/<int:author_id>", AuthorDetails.as_view(), name="author_details"),
    path('books/<int:book_id>', book_details, name="book_details") #gdy w GET po slash int następuje przypisanie do zmiennej book_id
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

