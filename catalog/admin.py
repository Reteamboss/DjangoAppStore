from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from catalog.models import Category, Product, Color, Display, Memory, Review, Quantity


class CustomMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 30


admin.site.register(Category, CustomMPTTModelAdmin)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','memory','color','price','quantity','image_url')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)
    list_filter = ('category','color','memory')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'rating',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id','color')
    # list_filter = ('due_back','status')

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('id','memory')
    # list_filter = ('due_back','status')

@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    list_display = ('id','display')
    # list_filter = ('due_back','status')

@admin.register(Quantity)
class QuantityAdmin(admin.ModelAdmin):
    list_display = ('id','product','quantity')
    # list_filter = ('due_back','status')

