from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_cat/$', views.create_cat, name='create_cat'),
    url(r'^info_book/$', views.info_book, name='info_book'),
    # url(r'^books/$', views.books, name='books'),
    # url(r'^authors/$', views.authors, name='authors'),
    # url(r'^category/$', views.category, name='category'),
    ##url(r'^books/$', views.BookListView.as_view(), name='books'),
    # url(r'^detail_books/$', views.BookDetailView.as_view(), name='detail_books'),
    url(r'^detail_books/(?P<pk>\d)/$', views.BookDetailView.as_view(), name='detail_books'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^category/$', views.CategoryListView.as_view(), name='category'),
    url(r'category/add/$', views.CategoryCreateView.as_view(), name='category_add'),
    url(r'^books/$', views.CategoryFormView.as_view(), name='books'),

]

