from django.urls import path
from . import views


urlpatterns = [
    path('bistro_items',views.bistro_items,name='bistro_items')
]