from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dietologs/', views.dietolog_list, name='dietologs'),
    path('dietologs/<int:dietolog_id>', views.dietolog_profile, name='dietolog_profile'),
    path('calcs/', views.calc_bzhu, name='calc_bzhu'),
]
