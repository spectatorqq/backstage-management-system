from django.urls import path
from article import views

urlpatterns = [
    path('save_article/', views.save_article),
    path('show_current_page/', views.show_current_page),
    path('update_article/', views.update_article),
    path('upload_pic/', views.upload_pic),
    path('pic_space/', views.pic_space),
    path('del_article/', views.del_article),
]
