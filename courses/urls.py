from django.urls import path
from .views import CourseUpdateAPIView

urlpatterns = [
    path('', CourseUpdateAPIView.as_view()),
]
