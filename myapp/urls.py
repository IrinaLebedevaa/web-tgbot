from django.urls import path
from .views import home, ozon1

urlpatterns = [
    path('', home, name='home'),  # главная страница
    path('ozon1', ozon1, name='ozon1'),
]