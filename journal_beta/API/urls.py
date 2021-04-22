from django.urls import path
from . import views

urlpatterns = [
    path('<int:group_number>/', views.index, name='index')
]
