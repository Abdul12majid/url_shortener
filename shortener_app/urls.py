from . import views
from django.urls import path

urlpatterns = [
    path('urls/', views.create_short_url, name='create_short_url'),
    path('urls/<str:short_code>/', views.resolve_short_url, name='resolve_short_url'),
    
]