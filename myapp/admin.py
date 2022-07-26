from django.contrib import admin
from .models import Product

# Register your models here.

admin.site.site_header = "Buy & Sell Website"
admin.site.site_title  = "ABC Buying"
admin.site.index_title = "Manage ABC Buying Website"


class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','price','desc')
    search_fields = ('name',)

admin.site.register(Product,ProductAdmin)


