from django.urls import path
from . import views

urlpatterns = [
        path('', views.button_view, name='main_view'),
        path('main_view', views.main_view, name='main_view'),
        path('hist_view', views.hist_view, name='hist_view'),
        path('bar_view', views.bar_view, name='bar_view'),
]
