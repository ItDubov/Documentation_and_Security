from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema

from .models import Course
from .serializers import CourseSerializer


@extend_schema(
    summary="Получить список курсов",
    description="Возвращает список всех курсов",
)
@extend_schema(
    methods=["POST"],
    summary="Создать курс",
    description="Создает новый курс",
)
class CourseListAPIView(ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
