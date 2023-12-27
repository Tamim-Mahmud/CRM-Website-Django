from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.reg_user,name='register'),
    path('record/<int:pk>',views.customer_record,name="record"),
    path('delete_record/<int:pk>',views.delete_customer_record,name="delete_record"),
    path('add_record',views.add_record,name="add_record")
    
]
