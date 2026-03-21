from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from drf_spectacular.utils import extend_schema

from .services import (
    create_product,
    create_price,
    create_session,
)

from .models import Payment


class PaymentCreateSerializer(serializers.Serializer):

    course = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


@extend_schema(
    summary="Создать оплату",
    description="Создает продукт, цену и сессию Stripe",
    request=PaymentCreateSerializer,
    responses={200: dict},
)
class CreatePaymentAPIView(APIView):

    def post(self, request):

        course_id = request.data.get("course")
        amount = request.data.get("amount")

        payment = Payment.objects.create(
            user=request.user,
            course_id=course_id,
            amount=amount,
        )

        product = create_product(payment.course.title)

        price = create_price(
            product.id,
            payment.amount,
        )

        session = create_session(price.id)

        payment.payment_url = session.url
        payment.save()

        return Response({
            "payment_url": session.url
        })
