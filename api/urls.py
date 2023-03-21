from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.get_all_books, name='all_books'),
    path('books/<int:book_id>', views.get_book_by_id, name='book_by_id'),
    path('cart/<int:user_id>/', views.cart, name='cart'),
    path('place_order/<int:user_id>/', views.place_order, name='place_order'),
]
