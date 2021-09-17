from django.urls import path
from . import views

urlpatterns = [
        path('', views.button_view, name='main_view'),
        path('main_view', views.main_view, name='main_view'),
]
