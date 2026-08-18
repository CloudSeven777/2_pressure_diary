from django.shortcuts import render

from .models import PressureRecord


def index(request):
    records = PressureRecord.objects.all().order_by("-created_at")
    return render(
        request,
        "pressure/index.html",
        {"records": records},
    )
