from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "first_name", "last_name", "email", "phone_number", "created_by")
    search_fields = ("customer_id", "phone_number")