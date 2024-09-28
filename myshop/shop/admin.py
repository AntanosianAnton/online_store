from django.contrib import admin
from .models import Category, Product, ProductImage, ProductSize, Size


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1  # Количество пустых строк для добавления новых записей


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5  # Количество дополнительных форм для изображений


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created',
                    'updated']
    list_filter = ['category', 'available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline]
    fields = ['category', 'name', 'slug', 'description', 'price', 'available',
              'sizechart']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
