from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Customer, Package, Payment
from .forms import AddCustomerForm

# Create your views here.
def CustomerDashboard(request):
    return render(request, 'umrah/dashboard.html')

# ------------------------------------
# ------------------------------------
# ----- customer CRUD operations ----- 
# ------------------------------------
# ------------------------------------

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "umrah/customer_list.html"
    context_object_name = "customers"
    paginate_by = 10
    
    def get_queryset(self):
        return Customer.objects.filter(
            is_active=True
        )


class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'umrah/customer_detail.html'
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = AddCustomerForm
    template_name = "umrah/customer_form.html"
    
    def form_valid(self, form):
        form.instance.created_by = (
            self.request.user
        )
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy(
            'umrah:customer-detail',
            kwargs = {
                "pk": self.object.pk
            }
        )
    
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model= Customer
    form_class = AddCustomerForm
    template_name = "umrah/customer_form.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "umrah:customer-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )

class CustomerArchiveView(LoginRequiredMixin, DeleteView):
    def post(self, request, pk):
        customer = get_object_or_404(
            Customer,
            pk=pk
        )
        customer.is_active = False
        customer.save()
        return redirect('umrah:customer-list')



class PackageList(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'umrah/package_list.html'
    context_object_name = "packages"

    
class PaymentList(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'umrah/payment_list.html'
    context_object_name = "payments"