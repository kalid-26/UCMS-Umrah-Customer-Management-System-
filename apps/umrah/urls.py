from django.urls import path
from .views import (
    
    DashboardView, 
    CustomerList, 
    CustomerDetail, 
    CustomerCreateView, 
    CustomerUpdateView, 
    CustomerArchiveView,
    
    ApplicationList,
    ApplicationDetail,
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationArchive,
    
    PaymentList,
    PaymentDetail,
    PaymentCreate,
    PaymentUpdate,
    PaymentArchive,
    
    PackageList, 
    PackageDetail,
    PackageCreate,
    PackageUpdate,
    PackageArchive)

app_name = 'umrah'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),  
    
    # customers urls 
    path('customers/', CustomerList.as_view(), name='customer-list'),  
    path('customers/detail/<int:pk>', CustomerDetail.as_view(), name='customer-detail'),  
    path('customers/create/', CustomerCreateView.as_view(), name='customer-add'),  
    path('customers/edit/<int:pk>', CustomerUpdateView.as_view(), name='customer-edit'),  
    path('customers/archive/<int:pk>', CustomerArchiveView.as_view(), name='customer-archive'),  
    
    # applications urls 
    path('applications/', ApplicationList.as_view(), name='application-list'),  
    path('applications/detail/<int:pk>', ApplicationDetail.as_view(), name='application-detail'),  
    path('applications/create/', ApplicationCreate.as_view(), name='application-add'),  
    path('applications/edit/<int:pk>', ApplicationUpdate.as_view(), name='application-edit'),  
    path('applications/archive/<int:pk>', ApplicationArchive.as_view(), name='application-archive'),  
    
    
    # package urls 
    path('packages/', PackageList.as_view(), name='package-list'),  
    path('packages/detail/<int:pk>', PackageDetail.as_view(), name='package-detail'),  
    path('packages/create/', PackageCreate.as_view(), name='package-add'),  
    path('packages/edit/<int:pk>', PackageUpdate.as_view(), name='package-edit'),  
    path('packages/archive/<int:pk>', PackageArchive.as_view(), name='package-archive'),  
    
    # payment urls 
    path('payments/', PaymentList.as_view(), name='payment-list'), 
    path('payments/detail/<int:pk>', PaymentDetail.as_view(), name='payment-detail'),  
    path('payments/create/', PaymentCreate.as_view(), name='payment-add'),  
    path('payments/edit/<int:pk>', PaymentUpdate.as_view(), name='payment-edit'),  
    path('payments/archive/<int:pk>', PaymentArchive.as_view(), name='payment-archive'),  
]
