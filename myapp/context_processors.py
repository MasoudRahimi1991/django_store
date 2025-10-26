from .models import Category, Cart, CartItem

def cart_count(request):
    # تعداد آیتم‌های سبد خرید کاربر
    cart_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_count = sum(ci.quantity for ci in CartItem.objects.filter(cart=cart))

    # فقط کتگوری‌های فعال
    categories = Category.objects.filter(is_enabled=True).order_by('name')

    return {
        'cart_count': cart_count,
        'categories': categories,
    }
