from django.contrib import admin
from .models import Customer, Package, UmrahApplication, Payment

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
    
@admin.register(UmrahApplication)
class UmrahApplicationAdmin(admin.ModelAdmin):
    list_display = ("customer", "package", "status",)
    list_filter = ("status", "package",)
    search_fields = ("customer__customer_id", "customer__first_name", "customer__last_name")
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("application", "amount", "payment_method", "payment_date")
    list_filter = ("payment_method",)