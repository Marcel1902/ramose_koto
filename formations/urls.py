from django.urls import path
from . import views

app_name = 'formation'

urlpatterns = [
    path('', views.formation_views, name='formation'),
    path('formation/<int:formation_id>/', views.formation_detail, name='formation_detail'),
    path('module/<int:module_id>/',views.formation_module_detail,name='affichage_detail_module')
]