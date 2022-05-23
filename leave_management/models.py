from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class LeaveRequest(models.Model):
    text = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150, default='Pending')
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(default=timezone.now)
    color_code = models.CharField(max_length=150, default='YELLOW')

    # def __str__(self):
    #     return self.text