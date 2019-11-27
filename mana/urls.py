from django.urls import path
from mana import views

urlpatterns = [
    path('home/', views.home),
    path('login/', views.login),
    path('send_code/', views.send_code),
    path('login_logic/', views.login_logic),
]
