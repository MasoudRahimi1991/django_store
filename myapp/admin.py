from django.contrib import admin
from .models import Category, Product, ProductImage, UserProfile, Order, Cart, CartItem


# ========================
# Inline Image for Product
# ========================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  


# ========================
# Category Admin
# ========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_enabled', 'created_at', 'updated_at')
    list_filter = ('is_enabled', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


# ========================
# Product Admin
# ========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'is_enabled', 'created_at')
    list_display_links = ('name',)
    list_filter = ('category', 'is_enabled')
    search_fields = ('name', 'category__name')
    ordering = ('-created_at',)
    inlines = [ProductImageInline]


# ========================
# ProductImage Admin
# ========================
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'uploaded_at')


# ========================
# User Profile Admin
# ========================
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


# ========================
# Order Admin
# ========================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_price', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'product__name')
    ordering = ('-order_date',)
    list_editable = ('status',) 

# ========================
# Cart Admin
# ========================
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)


# ========================
# CartItem Admin
# ========================
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
