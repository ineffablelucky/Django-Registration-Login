from django.urls import path, include
from home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home_index'),

]
