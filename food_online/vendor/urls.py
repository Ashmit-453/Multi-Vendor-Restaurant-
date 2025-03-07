from django.urls import path,include
from . import views
from accounts import views as Accountviews

urlpatterns = [
    path('',Accountviews.vendorDashboard,name="vendor"),
    path('profile/',views.vprofile,name="vprofile"),
    path('menu-builder/',views.menu_builder,name="menu_builder"),
    path('menu-builder/category/<int:pk>/',views.fooditems_by_category,name="fooditems_by_category"),
    path('menu-builder/category/add_category/',views.add_category,name="add_category"),
    path('menu-builder/category/edit_category/<int:pk>/',views.edit_category,name="edit_category"),
    path('menu-builder/category/delete_category/<int:pk>/',views.delete_category,name="delete_category"),
    path('menu-builder/food/add/',views.add_food,name="add_food"),
    path('menu-builder/food/edit_food/<int:pk>/',views.edit_food,name="edit_food"),
    path('menu-builder/food/delete_food/<int:pk>/',views.delete_food,name="delete_food"),

]
