from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path ('', views.home, name='home'),
    path ('th/', views.th, name='th'),
    path ('smile/', views.smile, name='smile'),
    path ('upload/',views.upload, name='upload'),
    # path ('button/', views.button, name='button'),
]

urlpatterns += staticfiles_urlpatterns()