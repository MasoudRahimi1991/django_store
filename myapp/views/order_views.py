from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from ..models import Order



@login_required
def order_history_view(request):
    """نمایش تاریخچه سفارش‌های کاربر"""
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'user/order_history.html', {'orders': orders})



@login_required
def order_delete_view(request, order_id):
  
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('order_history')


ر
@login_required
def order_update_view(request, order_id):
    """تغییر تعداد سفارش و به‌روزرسانی مبلغ"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity > 0:
                order.quantity = quantity
                order.total_price = order.product.price * quantity
                order.save()
        except (ValueError, TypeError):
            pass  
    return redirect('order_history')

@login_required
def order_detail_view(request, order_id):
    
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'user/order_detail.html', {'order': order})


@login_required
def payment_view(request):
  
    orders = Order.objects.filter(user=request.user, status='pending')
    total_amount = sum(order.total_price for order in orders)

    context = {
        'orders': orders,
        'total_amount': total_amount,
    }
    return render(request, 'user/payment.html', context)



@csrf_exempt
@login_required
def process_payment_view(request):
    """پرداخت سفارش‌های pending و تغییر وضعیت به paid"""
    if request.method == 'POST':
        orders = Order.objects.filter(user=request.user, status='pending')
        for order in orders:
            order.status = 'paid'
            order.save()
        return redirect('order_history')

    return redirect('payment')



@login_required
def order_cancel_view(request, order_id):
   
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'pending':
        order.status = 'cancelled'
        order.save()
    return redirect('order_history')
