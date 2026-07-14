from django.urls import path
from .views import LoginView, DashboardView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(), name='login'), 
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  
    
    path('logout/', LogoutView.as_view(), name='logout'),  
    
    # path('register/', RegisterView, name='register'),  
]
