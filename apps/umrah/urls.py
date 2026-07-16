from django.urls import path
from .views import CustomerList, CustomerDashboard, CustomerDetail, CustomerCreateView, CustomerUpdateView, CustomerArchiveView, PackageList, PaymentList

app_name = 'umrah'

urlpatterns = [
    path('', CustomerDashboard, name='customer-dashboard'),  
    
    # customers urls 
    path('customers/', CustomerList.as_view(), name='customer-list'),  
    path('customers/detail/<int:pk>', CustomerDetail.as_view(), name='customer-detail'),  
    path('customers/create/', CustomerCreateView.as_view(), name='customer-add'),  
    path('customers/edit/<int:pk>', CustomerUpdateView.as_view(), name='customer-edit'),  
    path('customers/archive/<int:pk>', CustomerArchiveView.as_view(), name='customer-archive'),  
    
    
    # package urls 
    path('packages/', PackageList.as_view(), name='package-list'),  
    
    
    # payment urls 
    path('payments/', PaymentList.as_view(), name='payment-list'),  
]
