from django.urls import path
from django.contrib.auth import views as auth_views
from .views import * 

urlpatterns = [
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logout_user, name="logout"),

    path('', home, name="home"),
    path('user/', user_page, name='user-page'),
    path('account/', account_settings, name="account"),
    path('products/', products, name="products"),
    path('customer/<str:pk_test>', customer, name="customer"),

    path('create_order/<str:pk>',create_order, name="createOrder" ),
    path('update_order/<str:pk>', update_order, name="updateOrder"),
    path('delete_order/<str:pk>', delete_order, name="deleteOrder"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
             name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),



]

