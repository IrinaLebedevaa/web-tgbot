from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from .models import ButtonClickStat

def home(request):
    return render(request, 'index.html')  # здесь открываем html

def ozon2(request):
    return render(request, 'ozon2.html')  # здесь открываем html

@csrf_exempt
def track_click(request):
    if request.method != "POST":
        return JsonResponse({"status": "error", "message": "Only POST allowed"})

    button_name = request.POST.get("button_name")
    if not button_name:
        return JsonResponse({"status": "error", "message": "button_name is required"})

    today = timezone.now().date()

    stat, created = ButtonClickStat.objects.get_or_create(
        date=today,
        button_name=button_name,
        defaults={"clicks": 0}
    )

    ButtonClickStat.objects.filter(id=stat.id).update(clicks=F("clicks") + 1)
    return JsonResponse({"status": "ok"})