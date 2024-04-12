from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #path('', views.index),
    path('bugs/', views.bug_list, name='bugs_list'),
    path('features/', views.feature_list, name='features_list'),
    #path('bugs/<int:bug_id>/', views.bug_detail, name='bugs_detail'),
    #path('features/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/<int:bug_id>/', views.BugsDetailView.as_view(), name='bugs_detail'),
    path('features/<int:feature_id>/', views.FeaturesDetailView.as_view(), name='feature_detail'),
]
