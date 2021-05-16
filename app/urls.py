from django.urls import path
from . import views


urlpatterns = [
    path("", views.AudioFileAPIView.as_view(), name="add-audio-file"),
    path("<str:file_type>/<int:pk>", views.AudioFileAPIView.as_view(), name="add-audio-file"),

]