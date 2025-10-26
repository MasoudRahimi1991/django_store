from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Product, ProductImage, Order,Favorite,Review
from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Count
from myapp.models import Product, ProductImage, Review, Favorite

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = ProductImage.objects.filter(product=product)
    reviews = Review.objects.filter(product=product).order_by('-created_at')

    # بررسی اینکه کاربر این محصول را در علاقه‌مندی‌ها دارد یا نه
    user_favorited = False
    if request.user.is_authenticated:
        user_favorited = Favorite.objects.filter(user=request.user, product=product).exists()

    # محاسبه میانگین امتیاز و تعداد نظرات
    review_stats = reviews.aggregate(avg_rating=Avg('rating'), review_count=Count('id'))
    avg_rating = review_stats['avg_rating'] or 0
    review_count = review_stats['review_count'] or 0

    # گرد کردن میانگین به عدد صحیح برای نمایش ستاره‌ها
    avg_rating_rounded = int(round(avg_rating))

    context = {
        'product': product,
        'images': images,
        'reviews': reviews,
        'user_favorited': user_favorited,
        'avg_rating': avg_rating_rounded,   # ⭐ برای نمایش ستاره‌های پر
        'review_count': review_count,       # 📊 برای نمایش تعداد نظرات
    }
    return render(request, 'shop/product_detail.html', context)


#  Add / Remove Favorite ❤️
# ============================
@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if not created:
        favorite.delete()
        messages.info(request, f"{product.name} removed from favorites.")
    else:
        messages.success(request, f"{product.name} added to favorites!")
    return redirect('product_detail', product_id=product.id)


# ============================
#  Add Review 💬
# ============================
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        Review.objects.create(
            user=request.user,
            product=product,
            rating=rating,
            comment=comment
        )
        messages.success(request, "Your review has been added!")
    return redirect('product_detail', product_id=product.id)