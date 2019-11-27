from django.urls import path
from userapp import views

urlpatterns = [
    path('save_user/', views.save_user),
    path('show_current_page/', views.show_current_page),
    path('edit_user/', views.edit_user),
    path('get_map_data/', views.get_map_data),
    path('get_data/', views.get_data),
    path('test/', views.test),

]
