from django.urls import path
from . import views

urlpatterns = [
    path('getgroup/<got_group_number>/', views.get_group_schedule, name='get_group_schedule'),
    path('weektype/', views.week_type, name='week_type'),
    path('', views.api_main_page, name='api_main_page')
]
