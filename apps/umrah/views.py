from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.db.models import Sum, Q

from .models import Customer, Package, Payment, UmrahApplication
from .forms import CustomerForm, ApplicationForm, PaymentForm, PackageForm

# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context["total_customers"] = (
            Customer.objects.filter(
                is_active=True
            ).count()
        )
        
        context["total_applications"] = (
            UmrahApplication.objects.filter(
                is_active=True
            ).count()
        )
        
        context["total_payments"] = (
            Payment.objects.filter(
                is_active=True
            ).count()
        )
        
        total_revenue = Payment.objects.filter(
            is_active=True
        ).aggregate(
            total=Sum("amount")
        )
        
        context["total_revenue"]=(
            total_revenue["total"] or 0
        )
        
        return context

# ------------------------------------
# ------------------------------------
# ----- customer CRUD operations ----- 
# ------------------------------------
# ------------------------------------

class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "umrah/customers/customer_list.html"
    context_object_name = "customers"
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Customer.objects.filter(
            is_active=True
        )
        
        search_query = (
            self.request.GET.get("search", "")
            .strip()
        )
        
        if search_query:
            queryset = queryset.filter(
                Q(customer_id__icontains = search_query) |
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(phone_number__icontains=search_query) |
                Q(passport_number__icontains=search_query) 
            )
        
        return queryset

class CustomerDetail(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'umrah/customers/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "umrah/customers/customer_form.html"
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response =  super().form_valid(form)

        messages.success(self.request, "Customer created successfully.")
        
        return response
    
    def get_success_url(self):
        return reverse_lazy(
            'umrah:customer-detail',
            kwargs = {
                "pk": self.object.pk
            }
        )
    
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model= Customer
    form_class = CustomerForm
    template_name = "umrah/customers/customer_form.html"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        messages.success(self.request, "Customer updated successfully.")

        return response
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
        
        messages.success(request, "Customer archived successfully.")
        
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
        query_set =  UmrahApplication.objects.filter(
            is_active=True
        )
        
        search_query = (
            self.request.GET.get("search", "")
            .strip()
        )
        
        if search_query:
            query_set = query_set.filter(
                Q(customer__customer_id__icontains=search_query) |
                Q(customer__first_name__icontains=search_query) |
                Q(customer__last_name__icontains=search_query) |
                Q(package__name__icontains=search_query) |
                Q(status__icontains=search_query)
            )
        return query_set
    
class ApplicationDetail(LoginRequiredMixin, DetailView):
    model = UmrahApplication
    template_name = "umrah/applications/application_detail.html"
    context_object_name = "application"

class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = UmrahApplication
    form_class = ApplicationForm
    template_name = "umrah/applications/application_form.html"
    
    def form_valid(self, form):
        form.instance.created_by = (self.request.user) 
        response = super().form_valid(form)
        
        messages.success(self.request, "Application created successfully.")
        
        return response 
    
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
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Application updated successfully.")
        
        return response
    
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
        messages.success(request, "Customer Arichived successfully.")
        return redirect("umrah:application-list")


# ------------------------------------
# ------------------------------------
# ----- package CRUD operations ------
# ------------------------------------
# ------------------------------------
class PackageList(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'umrah/packages/package_list.html'
    context_object_name = "packages"

    def get_queryset(self):
        return Package.objects.filter(
            is_active=True
        )
        
class PackageDetail(LoginRequiredMixin, DetailView):
    model = Package
    template_name = 'umrah/packages/package_detail.html'
    context_object_name = "package"

class PackageCreate(LoginRequiredMixin, CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'umrah/packages/package_form.html'
    
    def form_valid(self, form):
        form.instance.created_by = (self.request.user) 
        response = super().form_valid(form)
        
        messages.success(self.request, "Package created successfully.")
        
        return response 
    def get_success_url(self):
        return reverse_lazy(
            "umrah:package-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )
        
class PackageUpdate(LoginRequiredMixin, UpdateView):
    model = Package
    form_class = PackageForm
    template_name = 'umrah/packages/package_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Package updated successfully.")
        
        return response
    
    def get_success_url(self):
        return reverse_lazy(
            "umrah:package-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )
        
class PackageArchive(LoginRequiredMixin, DeleteView):
    def post(self, request, pk):
        package = get_object_or_404(
            Package,
            pk=pk
        )
        package.is_acitve = False
        package.save()
        messages.success(request, "Package Arichived successfully.")
        return redirect("umrah:package-list")


# ------------------------------------
# ------------------------------------
# ----- payments CRUD operations ------
# ------------------------------------
# ------------------------------------
class PaymentList(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'umrah/payments/payments_list.html'
    context_object_name = "payments"
    paginate_by = 5
    
    def get_queryset(self):
        query_set = Payment.objects.filter(
            is_active=True
        )

        search_query = (
            self.request.GET.get("search", "")
            .strip()
        )
        
        if search_query:
            query_set = query_set.filter(
                Q(application__customer__customer_id__icontains=search_query) |
                Q(application__customer__first_name__icontains=search_query) |
                Q(application__customer__last_name__icontains=search_query) |
                Q(reference_number__icontains=search_query) |
                Q(payment_method__icontains=search_query)
            )
        
        return query_set
    
class PaymentDetail(LoginRequiredMixin, DetailView):
    model = Payment
    template_name = 'umrah/payments/payments_detail.html'
    context_object_name = "payment"
    
class PaymentCreate(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'umrah/payments/payments_form.html'
    
    def form_valid(self, form):
        form.instance.created_by = (self.request.user) 
        response = super().form_valid(form)
        
        messages.success(self.request, "Payment created successfully.")
        
        return response 
    
    def get_success_url(self):
        return reverse_lazy(
            "umrah:payment-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )
    
class PaymentUpdate(LoginRequiredMixin, UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name =  'umrah/payments/payments_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Payment updated successfully.")
        
        return response
    
    def get_success_url(self):
        return reverse_lazy(
            "umrah:payment-detail",
            kwargs = {
                "pk": self.object.pk
            }
        )
        
class PaymentArchive(LoginRequiredMixin, DeleteView):
    def post(self, request, pk):
        payment = get_object_or_404(
            Payment,
            pk=pk
        )
        payment.is_active = False
        payment.save()
        messages.success(request, "Payment Arichived successfully.")
        return redirect("umrah:payment-list")