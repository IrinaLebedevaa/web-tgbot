from django.template.context_processors import static
from django.urls import path
from .views import home, ozon2, track_click

urlpatterns = [
    path('', home, name='home'),  # главная страница
    path('ozon2/', ozon2, name='ozon2'),
    path('track-click/', track_click, name="track_click"),
]
