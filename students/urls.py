from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('',views.affichage_formation, name='affichage_formation'),
    path('login/',views.login_user ,name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout')
]