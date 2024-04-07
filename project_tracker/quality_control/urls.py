from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('quality_control/', views.index),
    path('bugs/', views.bug_list, name='bugs_list'),
    path('features/', views.feature_list, name='features_list'),
    path('bug/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('feature/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail'),
]
