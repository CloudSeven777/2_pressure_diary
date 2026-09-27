from django.shortcuts import redirect, render

from .forms import PressureRecordForm
from .models import PressureRecord
from django.views.decorators.http import require_POST

def index(request):
    records = PressureRecord.objects.all().order_by("-created_at")
    return render(
        request,
        "pressure/index.html",
        {"records": records},
    )

def add_pressure(request):
    if request.method == "POST":
        form = PressureRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PressureRecordForm()

    return render(
        request,
        "pressure/add_pressure.html",
        {"form": form},
    )

@require_POST
def delete_pressure(request, record_id):
    record = PressureRecord.objects.get(id=record_id)
    record.delete()
    return redirect("index")