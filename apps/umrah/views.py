from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Customer, Package, Payment, UmrahApplication
from .forms import CustomerForm, ApplicationForm

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
    template_name = "umrah/customers/customer_list.html"
    context_object_name = "customers"
    paginate_by = 10
    
    def get_queryset(self):
        return Customer.objects.filter(
            is_active=True
        )


class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'umrah/customers/customer_detail.html'
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm, ApplicationForm
    template_name = "umrah/customers/customer_form.html"
    
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
    form_class = CustomerForm, ApplicationForm
    template_name = "umrah/customers/customer_form.html"
    
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


# ------------------------------------
# ------------------------------------
# ----- application CRUD operations --
# ------------------------------------
# ------------------------------------

class ApplicationList(LoginRequiredMixin, ListView):
    model = UmrahApplication
    template_name = "umrah/applications/application_list.html"
    context_object_name = "applications"
    paginate_by = 10

    def get_queryset(self):
        return UmrahApplication.objects.filter(
            is_active=True
        )
        
class ApplicationDetail(LoginRequiredMixin, DetailView):
    model = UmrahApplication
    template_name = "umrah/applications/application_detail.html"
    context_object_name = "application"

class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = UmrahApplication
    form_class = ApplicationForm
    template_name = "umrah/applications/application_form.html"
    
    def form_valid(self, form):
        form.instance.created_by = (
            self.request.user
        ) 
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy(
            "umrah:application-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )

class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model = UmrahApplication
    form_class = ApplicationForm
    template_name = "umrah/applications/application_form.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "umrah:application-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )

class ApplicationArchive(LoginRequiredMixin, DeleteView):
    def post(self, request, pk):
        application = get_object_or_404(
            UmrahApplication,
            pk=pk
        )        
        application.is_active = False 
        application.save()
        return redirect("umrah:application-list")



# ------------------------------------
# ------------------------------------
# ----- package CRUD operations ------
# ------------------------------------
# ------------------------------------
class PackageList(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'umrah/package_list.html'
    context_object_name = "packages"


# ------------------------------------
# ------------------------------------
# ----- payments CRUD operations ------
# ------------------------------------
# ------------------------------------
class PaymentList(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'umrah/payments/payments_list.html'
    context_object_name = "payments"