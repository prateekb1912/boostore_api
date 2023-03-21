import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Book, Order, User


def get_all_books(request):
    books = Book.objects.all()
    data = {"books": []}
    for book in books:
        data["books"].append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "price": book.price
        })
    return JsonResponse(data)

def get_book_by_id(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "price": book.price
    }
    return JsonResponse(data)

@csrf_exempt
def cart(request, user_id):
    if request.method == 'GET':
        orders = Order.objects.filter(user_id=user_id)
        return JsonResponse({'orders': list(orders.values())})
    elif request.method == 'POST':
        data = json.loads(request.body)
        book_id = data['book_id']
        quantity = data['quantity']
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=user_id)
        order = Order(user=user, book=book, quantity=quantity)
        order.save()
        return JsonResponse({'success': True})
    elif request.method == 'DELETE':
        data = json.loads(request.body)
        order_id = data['order_id']
        order = Order.objects.get(id=order_id)
        order.delete()
        return JsonResponse({'success': True})

@csrf_exempt
def place_order(request, user_id):
    orders = Order.objects.filter(user_id=user_id, placed_order=False)
    for order in orders:
        order.placed_order = True
        order.save()
    return JsonResponse({'success': True})
