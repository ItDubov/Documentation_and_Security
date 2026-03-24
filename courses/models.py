from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.title

class Subscription(models.Model):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.course}"
