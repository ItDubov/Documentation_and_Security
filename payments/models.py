from django.db import models
from users.models import User
from courses.models import Course


class Payment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stripe_product_id = models.CharField(
        max_length=255,
        blank=True
    )

    stripe_price_id = models.CharField(
        max_length=255,
        blank=True
    )

    stripe_session_id = models.CharField(
        max_length=255,
        blank=True
    )

    payment_url = models.URLField(blank=True)

    status = models.CharField(
        max_length=50,
        default="created"
    )
