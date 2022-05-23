from rest_framework import serializers
from .models import LeaveRequest

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ('id', 'text', 'status', 'employee', 
            'request_date', 'color_code',)
