from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    short_description = models.TextField()
    published_at = models.DateTimeField()
    cover = models.ImageField(null=True, blank=True)
    author = models.ManyToManyField(to="books.Author",verbose_name="authors",related_name="books")

    def __str__(self):
        return "Book: "+self.title


class Author(models.Model):
    first_name = models.CharField(verbose_name="name", max_length=100);
    last_name = models.CharField(verbose_name="surname", max_length=100);
    about = models.TextField(verbose_name="description", blank=True);
    photo = models.ImageField(verbose_name="image", blank=True);

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return self.first_name + " " + self.last_name


class Review(models.Model):
    book = models.ForeignKey(to="books.Book", verbose_name="Reviewed book", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Review's author", on_delete=models.RESTRICT)
    content = models.TextField(verbose_name="reviews")
    is_recommended = models.BooleanField(verbose_name="Is it good enough for others?")

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"

    def __str__(self):
        return  self.book.title + " added by " + self.reviewer.username