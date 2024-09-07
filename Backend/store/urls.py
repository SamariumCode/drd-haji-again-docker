from django.urls import path
from . import views

urlpatterns = [
    path('cache/', views.cache_test, name='cache_test'),
]
