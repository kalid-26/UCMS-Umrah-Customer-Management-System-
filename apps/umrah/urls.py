from django.urls import path
from .views import CustomerList, CustomerDashboard, CustomerDetail, PackageList, PaymentList

app_name = 'umrah'

urlpatterns = [
    path('', CustomerDashboard, name='customer-dashboard'),  
    
    # customers urls 
    path('customers/', CustomerList.as_view(), name='customer-list'),  
    path('customers/<int:pk>', CustomerDetail.as_view(), name='customer-detail'),  
    
    
    # package urls 
    path('packages/', PackageList.as_view(), name='package-list'),  
    
    
    # payment urls 
    path('payments/', PaymentList.as_view(), name='payment-list'),  
]
