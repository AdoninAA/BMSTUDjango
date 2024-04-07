from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('quality_control/', views.index),
    path('bugs/', views.bugs_page, name='bugs_page'),
    path('features/', views.features_page, name='features_page'),
]
