from django.urls import path

from . import views

app_name = 'delivery'
urlpatterns = [
    # ex: /polls/
    path('orders', views.order_list, name="orderlist"),
    # path('timeinput', views.time_input, name="timeinput"),
    # path('menus/<int:shop>', views.menu, name="menu"),   
    # path('order/',views.order,name="order")
        
]