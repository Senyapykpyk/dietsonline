from django.urls import path
from . import views

app_name="users"
urlpatterns = [
   	path('register/', views.register, name='register'), 
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('activate_profile/', views.activate_profile, name='activate_profile')
]

