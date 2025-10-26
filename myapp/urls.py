from django.urls import path
from django.contrib.auth import views as auth_views

# ========================
# Import Views
# ========================
from .views.home_views import HomeView
from .views.user_views import register_view,custom_logout_view
from .views.profile_views import profile_view, edit_profile_view
from .views import order_views

from .views.order_views import (
    order_history_view,
    order_delete_view,
    order_update_view,
    payment_view,
    process_payment_view,
    order_cancel_view

)
from .views.product_detail_views import product_detail_view,add_review,toggle_favorite
from .views.cart_views import (
    add_to_cart_view,
    view_cart_view,
    increase_quantity_view,
    decrease_quantity_view,
    remove_item_view,
    checkout_view
)
from .views import account_views  # ✅ جدید برای مسیرهای بخش Account
# from .views.account_views import account_dashboard_view


# ========================
# URL Patterns
# ========================
urlpatterns = [
    # ------------------------
    # 🏠 Home
    # ------------------------
    path('', HomeView.as_view(), name='home'),

    # ------------------------
    # 👤 Authentication
    # ------------------------
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', custom_logout_view, name='logout'),


    path('register/', register_view, name='register'),

    # ------------------------
    # 👤 User Profile
    # ------------------------
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),

    # ------------------------
    # 🧾 Orders
    # ------------------------
    path('orders/', order_history_view, name='order_history'),
    path('orders/delete/<int:order_id>/', order_delete_view, name='order_delete'),
    path('orders/update/<int:order_id>/', order_update_view, name='order_update'),
    path('orders/cancel/<int:order_id>/', order_cancel_view, name='order_cancel'),
    path('orders/payment/', payment_view, name='payment'),
    path('orders/process-payment/', process_payment_view, name='process_payment'),

    # ------------------------
    # 🛒 Cart
    # ------------------------
    path('cart/', view_cart_view, name='view_cart'),
    path('cart/add/<int:pk>/', add_to_cart_view, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', increase_quantity_view, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', decrease_quantity_view, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', remove_item_view, name='remove_item'),
    path('cart/checkout/', checkout_view, name='checkout'),

    # ------------------------
    # 🏷️ Product
    # ------------------------
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),

    # ------------------------
    # ⚙️ Account Section (Dashboard)
    # ------------------------
   path('account/orders/<int:order_id>/', order_views.order_detail_view, name='order_detail'),

 
    path('account/profile/', account_views.account_profile, name='account_profile'),
    path('account/orders/', account_views.account_orders, name='account_orders'),
    path('account/favorites/', account_views.account_favorites, name='account_favorites'),
    # path('account/settings/', account_views.account_settings, name='account_settings'),
    # path('account/', account_dashboard_view, name='account_dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login_alt'),


    # Favorites & Reviews
    path('product/<int:product_id>/favorite/', toggle_favorite, name='toggle_favorite'),
    path('product/<int:product_id>/review/add/', add_review, name='add_review'),

]
