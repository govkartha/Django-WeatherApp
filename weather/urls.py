from django.urls import path
from . import views

urlpatterns = [
    # path('', views.indexView.as_view(), name='index'),
    path('', views.indexView, name='home'),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]