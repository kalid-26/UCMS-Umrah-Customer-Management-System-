from django.urls import path
from .views import (
    
    CustomerList, 
    CustomerDashboard, 
    CustomerDetail, 
    CustomerCreateView, 
    CustomerUpdateView, 
    CustomerArchiveView,
    
    ApplicationList,
    ApplicationDetail,
    ApplicationCreate,
    ApplicationUpdate,
    ApplicationArchive,
    
    PackageList, 
    PaymentList)

app_name = 'umrah'

urlpatterns = [
    path('', CustomerDashboard, name='customer-dashboard'),  
    
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
    
    
    # payment urls 
    path('payments/', PaymentList.as_view(), name='payment-list'),  
]
