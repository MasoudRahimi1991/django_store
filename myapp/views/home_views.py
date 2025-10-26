from django.views.generic import ListView
from django.db.models import Q, Avg
from myapp.models import Product
from .base_views import BaseView


class HomeView(ListView, BaseView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
  
      
        queryset = Product.objects.filter(is_enabled=True).prefetch_related('reviews')

        # 🔍 فیلتر جستجو (در نام یا توضیح)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

       
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)


        for product in queryset:
            avg_rating = product.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
            product.avg_rating = round(avg_rating, 1)

       
            product.review_count = product.reviews.count()

        return queryset

    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_category'] = self.request.GET.get('category', '')
        return context



