from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('mycars' , views.profile, name='profile'),
    path('test/new/',views.new_carTest,name='new_car2'),
    path('payment/<int:v_n>/new',views.new_payment,name='new_pymnt'),
    path('p/<int:v_n1>',views.pay_done,name='pay_done'),


    
]
