from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Product, Cart, CartItem,Order
from django.utils import timezone

@login_required
def add_to_cart_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    return redirect('view_cart')


@login_required
def view_cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})


@login_required
def increase_quantity_view(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity += 1
    item.save()
    return redirect('view_cart')


@login_required
def decrease_quantity_view(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('view_cart')


@login_required
def remove_item_view(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('view_cart')


@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    if not items:
        # اگر سبد خرید خالی بود
        return redirect('view_cart')

    for item in items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.total_price(),
            order_date=timezone.now()
        )

    # بعد از انتقال سفارش‌ها، سبد خرید خالی می‌شود
    cart.items.all().delete()

    return redirect('order_history')