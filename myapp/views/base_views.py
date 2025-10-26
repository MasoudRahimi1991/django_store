from django.views.generic import View
from ..models import Category

class BaseView(View):
    """
    کلاس پایه برای تمام ویوهای سایت.
    هر ویو که از این کلاس ارث ببرد، به‌طور خودکار
    اطلاعات عمومی مانند دسته‌بندی‌ها، وضعیت کاربر و ... را دریافت می‌کند.
    """

    def get_context_data(self, **kwargs):
        # این خط باعث می‌شود context اصلی (مثلاً محصولات در ListView) حفظ شود ✅
        context = super().get_context_data(**kwargs)

        # فقط کتگوری‌های فعال
        context['categories'] = Category.objects.filter(is_enabled=True)

        # مقادیر عمومی
        context['cart_count'] = 0
        context['favorite_count'] = 0

        # اطلاعات کاربر در صورت لاگین بودن
        context['user'] = self.request.user if self.request.user.is_authenticated else None

        return context
