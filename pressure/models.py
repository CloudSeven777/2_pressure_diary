from django.db import models

class PressureRecord(models.Model):
    systolic = models.PositiveIntegerField()
    diastolic = models.PositiveIntegerField()
    pulse = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.systolic}/{self.diastolic}, пульс {self.pulse}"



