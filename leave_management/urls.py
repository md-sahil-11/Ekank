from .views import LeaveView
# from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'leave_management'

router = DefaultRouter()
router.register('leave', LeaveView, basename='leave')
urlpatterns = router.urls