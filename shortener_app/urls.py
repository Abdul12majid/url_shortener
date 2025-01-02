from . import views
from django.urls import path

urlpatterns = [
    path('urls/', views.create_short_url, name='create_short_url'),
    
]