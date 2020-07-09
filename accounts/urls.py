from django.urls import path
from .views import * 

urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logout_user, name="logout"),

    path('', home, name="home"),
    path('user/', user_page, name='user-page'),
    path('products/', products, name="products"),
    path('customer/<str:pk_test>', customer, name="customer"),

    path('create_order/<str:pk>',createOrder, name="createOrder" ),
    path('update_order/<str:pk>', updateOrder, name="updateOrder"),
    path('delete_order/<str:pk>', deleteOrder, name="deleteOrder")


]
