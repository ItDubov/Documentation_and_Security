from django.urls import path
from .views import CreatePaymentAPIView

urlpatterns = [
    path("pay/", CreatePaymentAPIView.as_view()),
]
