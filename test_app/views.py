from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Caterogy, Author
from django.template import loader


def index(request):
    # return HttpResponse("Hello, world!")
    books = Book.objects.all()
    return render(request, 'test_app/index.html',
                  {'books': books})


def create_cat(request):
    # return HttpResponse("Hello, world!")
    if request.method == "POST":
        Caterogy.objects.create(title=request.POST['title'], description=request.POST['description'])
    cat = Caterogy.objects.all()
    return render(request, 'test_app/form_author.html', {'cats': cat})


def info_book(request):
    # book_info = Book.objects.get(pk=1)
    # return render(request, 'test_app/books.html', {'book_info': book_info})
    t = loader.get_template('test_app/info_books.html')
    c = {'books': Book.objects.all().prefetch_related('authors')}
    return HttpResponse(t.render(c, request))


def category(request):
    # return HttpResponse("Hello, world!")
    categories = Caterogy.objects.all()
    return render(request, 'test_app/category.html',
                  {'categories': categories})


def authors(request):
    # return HttpResponse("Hello, world!")
    authors = Author.objects.all()
    return render(request, 'test_app/authors.html',
                  {'authors': authors})


def books(request):
    # return HttpResponse("Hello, world!")
    books = Book.objects.all()
    return render(request, 'test_app/books.html',
                  {'books': books})