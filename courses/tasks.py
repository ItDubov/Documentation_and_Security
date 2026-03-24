from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_update_email(email, course_title):

    send_mail(
        subject="Course updated",
        message=f"Course '{course_title}' has been updated",
        from_email=None,
        recipient_list=[email],
    )
