from django.urls import path
from banner import views

urlpatterns = [
    path('save_banner/', views.save_banner),
    path('show_current_page/', views.show_current_page),
    path('edit_carousel/', views.edit_carousel)
]