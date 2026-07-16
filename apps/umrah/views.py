from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer, Package, Payment

# Create your views here.
def CustomerDashboard(request):
    return render(request, 'umrah/dashboard.html')

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "umrah/customer_list.html"
    context_object_name = "customers"
    paginate_by = 10
    
    
class PackageList(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'umrah/package_list.html'
    context_object_name = "packages"
    
class PaymentList(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'umrah/payment_list.html'
    context_object_name = "payments"