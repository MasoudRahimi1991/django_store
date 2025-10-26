from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .order_views import order_history_view  
from myapp.models import Order, UserProfile ,Favorite 

@login_required
def account_dashboard(request):
    return render(request, 'user/account_dashboard.html')

@login_required
def account_profile(request):
    return render(request, 'user/account_profile.html')

@login_required
def account_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'user/account_orders.html', {'orders': orders})

@login_required
def account_favorites(request):
    # فعلاً صفحه خالی — بعداً مدل Favorite رو اضافه می‌کنیم
    return render(request, 'user/account_favorites.html')



@login_required
def account_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('product')
    return render(request, 'user/account_favorites.html', {'favorites': favorites})





# @login_required
# def account_settings(request):
#     profile = UserProfile.objects.filter(user=request.user).first()
#     return render(request, 'user/account_settings.html', {'profile': profile})
