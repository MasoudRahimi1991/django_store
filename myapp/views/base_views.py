from django.views.generic import View
from ..models import Category

class BaseView(View):
 

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)

        
        context['categories'] = Category.objects.filter(is_enabled=True)

        
        context['cart_count'] = 0
        context['favorite_count'] = 0

        
        context['user'] = self.request.user if self.request.user.is_authenticated else None

        return context
