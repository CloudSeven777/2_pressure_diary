from django import forms

from .models import PressureRecord


class PressureRecordForm(forms.ModelForm):
    class Meta:
        model = PressureRecord
        fields = ["systolic", "diastolic", "pulse"]