from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=pid)
        cart_items.append({
            'product': product,
            'quantity': qty,
            'subtotal': product.price * qty
        })
        total += product.price * qty
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total': total})
