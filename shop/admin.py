from django.contrib import admin
from.models import *
# Register your models here.

admin.site.site_header ='E-commerce'
admin.site.site_title =' SBC shop'
admin.site.index_title = "Manageur"
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','category','date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommander(admin.ModelAdmin):
    list_display = ('items','nom','email','adresse','ville','pays','total','zipcode','date_commande')

admin.site.register(Category, AdminCategory)
admin.site.register(Product,  AdminProduct)
admin.site.register(Commander, AdminCommander)