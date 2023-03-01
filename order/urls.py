from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    # ex: /polls/
    path('shops/', views.shop, name="shop"),
    path('menus/<int:shop>', views.menu, name="menu"),   
    path('order/',views.order,name="order") 
]