from django.urls import path
from . import views

urlpatterns = [
    path('', views.formation_views, name='formation'),
    path('formation/<int:formation_id>/', views.formation_detail, name='formation_detail'),
]