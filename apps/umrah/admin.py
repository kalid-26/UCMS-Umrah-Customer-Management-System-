from django.contrib import admin
from .models import Customer, Package

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "first_name", "last_name", "email", "phone_number", "created_by",)
    search_fields = ("first_name", "last_name","customer_id", "phone_number",)
    
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description",)
    list_filter = ("is_active",)
    search_fields = ("name",)