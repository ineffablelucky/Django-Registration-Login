from django.urls import path, include
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete
)

urlpatterns = [
    path('contact/', views.contact_page, name = 'contact_page'),
    path('login/', login, {'template_name' : 'ImageAccount/login.html'}, name='login'),
    path('logout/', logout, {'template_name' : 'ImageAccount/logout.html'}, name='logout'),
    path('', views.useraccount, name = 'useraccount'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.view_profile, name= 'view_profile'),
    path('profile/edit/', views.edit_profile, name= 'edit_profile'),

    # check for https://docs.djangoproject.com/en/2.0/topics/auth/default/
    # in later projects
    path('change-password/', views.change_password, name= 'change_password'),

    path('reset-password/', password_reset , {'template_name' : 'ImageAccount/reset_password.html',
    'email_template_name' : 'ImageAccount/reset_password_email.html'} ,name= 'password_reset'),

    path('reset-password/done/', password_reset_done,
    {'template_name' : 'ImageAccount/reset_password_done.html'} ,
     name= 'password_reset_done'),

    path('reset-password/confirm/<uidb64>/<token>/', password_reset_confirm,
    {'template_name' : 'ImageAccount/reset_password_confirm.html'},
    name= 'password_reset_confirm'),

    path('reset-password/complete/', password_reset_complete,
    {'template_name' : 'ImageAccount/reset_password_complete.html'},
    name= 'password_reset_complete'),
]
