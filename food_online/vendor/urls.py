from django.urls import path,include
from . import views
from accounts import views as Accountviews

urlpatterns = [
    path('',Accountviews.vendorDashboard,name="vendor"),
    path('profile/',views.vprofile,name="vprofile"),
    
]