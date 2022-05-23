from leave_management.models import LeaveRequest
from leave_management.serializers import LeaveSerializer
from rest_framework.permissions import BasePermission
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ActionBasedPermission(BasePermission):
    def has_permission(self, request, view):
        # print('action', view.action)
        user = request.user
        if not user.is_staff and view.action in ['list', 'create', 'retrieve']:
            return user.is_authenticated 
        if view.action in ['list', 'update', 'retrieve', 'destroy']:
            return user.is_staff
        return False


class LeaveView(viewsets.ModelViewSet):
    serializer_class = LeaveSerializer
    permission_classes = [ActionBasedPermission,]


    def get_queryset(self):
        if self.request.user.is_staff:
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(employee=self.request.user.id)
    

    def list(self, request):
        queryset = self.get_queryset()
        print(queryset)
        serializer = LeaveSerializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        data = {}
        data.update(request.data)
        data['employee'] = request.user.id
        data['status'] = 'Pending'
        data['color_code'] = 'YELLOW'

        serializer = LeaveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, pk=None):
        if not pk:
            return Response({'msg': 'No Content'}, status=status.HTTP_204_NO_CONTENT)
        leave = get_object_or_404(LeaveRequest, id=pk)
        data = {}
        data.update(request.data)
        status_code = {
            'Accepted': 'GREEN',
            'Rejected': 'RED',
            'Pending': 'YELLOW'
        }
        data['color_code'] = status_code[data['status']]

        serializer = LeaveSerializer(leave, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk=None):
        if not pk:
            return Response({'msg': 'No Content'}, status=status.HTTP_204_NO_CONTENT)
        leave = get_object_or_404(LeaveRequest, id=pk)
        leave.delete()
        return Response({'msg': 'Request deleted'}, status=status.HTTP_200_OK)