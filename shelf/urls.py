from django.urls import path
# from .models import
from .views import authordetailview, authorlistview, booklistview, publisherlistview, index
# from views import , AuthorListView, BookListView, PublisherListView
# from shelf.views import AuthorListView, BookListView, PublisherListView, AuthorDetailView
urlpatterns = [
    path('authors/', authorlistview.AuthorListView.as_view(), name='author-list'),
    path('authors/<pk>', authordetailview.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', booklistview.BookListView.as_view(), name='author-list'),
    path('publishers/', publisherlistview.PublisherListView.as_view()),
    path('',  index.index, name='index'),
]