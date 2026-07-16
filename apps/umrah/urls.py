from django.urls import path
from .views import CustomerList, CustomerDashboard, PackageList, PaymentList

app_name = 'umrah'

urlpatterns = [
    path('', CustomerDashboard, name='customer-dashboard'),  
    
    path('customers/', CustomerList.as_view(), name='customer-list'),  
    
    path('packages/', PackageList.as_view(), name='package-list'),  
    
    path('payments/', PaymentList.as_view(), name='payment-list'),  
]
