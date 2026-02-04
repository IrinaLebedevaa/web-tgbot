from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # здесь открываем html

def ozon2(request):
    return render(request, 'ozon2.html')  # здесь открываем html