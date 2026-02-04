from django.urls import path
from .views import home, ozon2

urlpatterns = [
    path('', home, name='home'),  # главная страница
    path('ozon2/', ozon2, name='ozon2'),
]
