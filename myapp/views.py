from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # здесь открываем html

def ozon1(request):
    return render(request, 'ozon1.html')  # здесь открываем html