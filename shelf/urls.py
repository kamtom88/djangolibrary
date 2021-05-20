from django.urls import path

from .views import authordetailview, authorlistview, booklistview, publisherlistview, index,\
    contact_view, bookdetailview, rentalview

urlpatterns = [
    path('authors/', authorlistview.AuthorListView.as_view(), name='author-list'),
    path('authors/<pk>', authordetailview.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', booklistview.BookListView.as_view(), name='book-list'),
    path('books/<pk>', bookdetailview.BookDetailView.as_view(), name='book-detail'),
    path('publishers/', publisherlistview.PublisherListView.as_view()),
    path('', index.MainPage.as_view(), name='index'),
    # path('',  index.index, name='index'),
    path('contact/',  contact_view.MessageAddView.as_view(), name='contact'),
    path('rental/',  rentalview.RentalView.as_view(), name='rental'),
]