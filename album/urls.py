from django.urls import path
from album import views

urlpatterns = [
    path('save_album/', views.save_album),
    path("show_current_page/", views.show_current_page),
    path("edit_album/", views.edit_album),
    path("save_audio/", views.save_audio),
    path("get_audio_by_albumid/", views.get_audio_by_albumid),
    path("edit_audio/", views.edit_audio),
]
