from django.urls import path
from authority import views

urlpatterns = [
    path('show_current_staff/', views.show_current_staff),
    path('login/', views.login),
    path('login_logic/', views.login_logic),
]
