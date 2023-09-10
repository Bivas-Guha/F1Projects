from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('upload_xl', views.upload_xl, name='upload_xl'),
    path('edit_file', views.edit_file, name='edit_file'),
    path('convert_file', views.convert_file, name='convert_file'),
]
