from rest_framework.generics import UpdateAPIView
from drf_spectacular.utils import extend_schema

from .models import Course
from .serializers import CourseSerializer

from django.utils import timezone
from datetime import timedelta

from .tasks import send_update_email
from .models import Subscription


@extend_schema(
    summary="Получить список курсов",
    description="Возвращает список всех курсов",
)
@extend_schema(
    methods=["POST"],
    summary="Создать курс",
    description="Создает новый курс",
)

class CourseUpdateAPIView(UpdateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_update(self, serializer):

        course = self.get_object()

        # проверка 4 часа
        if course.updated_at and (
            course.updated_at > timezone.now() - timedelta(hours=4)
        ):
            serializer.save()
            return

        serializer.save()

        # подписки
        subs = Subscription.objects.filter(
            course=course,
            is_active=True,
        )

        for sub in subs:

            send_update_email.delay(
                sub.user.email,
                course.title,
            )
