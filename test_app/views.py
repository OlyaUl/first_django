from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Caterogy, Author
from django.template import loader
from django.views.generic import View, ListView, CreateView, DetailView, FormView
from django.utils import timezone
from .forms import CategoryForm


class BookListView(ListView):
    template_name = 'test_app/list.html'
    model = Book
    context_object_name = 'books'


class CategoryListView(ListView):
    template_name = 'test_app/category_list.html'
    model = Caterogy
    context_object_name = 'categories'


class AuthorListView(ListView):
    template_name = 'test_app/authors_list.html'
    model = Author
    context_object_name = 'authors'


class CategoryCreateView(ListView):
    model = Caterogy
    fields = ['title']


class CategoryFormView(FormView):
    form_class = CategoryForm
    template_name = 'test_app/form_category.html'
    success_url = '/test_app/category/'

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)

        return self.form_invalid(form)


class BookDetailView(DetailView):
    template_name = 'test_app/detail_book.html'
    '''
    model = Book
    context_object_name = 'books'
    pk_url_kwarg = 'pk'''
    model = Book
    # slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



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
