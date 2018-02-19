from django.contrib import admin
from django.urls import path, include
from Tutorial import views
from django.conf import settings
from django.conf.urls.static import static
import home

urlpatterns = [

    # below accounts.login is redirected with help of settings.LOGIN_
    #path('accounts/login/', views.reset_login_redirect, name='reset_login_redirect'),
    #path('', views.useraccount_homepage_redirect, name='useraccount_homepage_redirect'),
    path('useraccount/', include('ImageAccount.urls'), name='useraccount_homepage'),
    path('home/', include('home.urls'), name='home_homepage'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
