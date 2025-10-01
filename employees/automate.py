from django.conf import settings
from .models import Employee
from django.db.models import Avg
from django.core.mail import send_mail

def send_salary_report():
    avg_salary = Employee.objects.aggregate(avg=Avg("salary"))["avg"] or 0

    subject = "Weekly Salary Report"
    message = f"The average salary this week is: {avg_salary:.2f} USD"

    send_mail(
        subject=subject,
        message=message,
        from_email="noreply@peopleflow.com",
        recipient_list=["boss@company.com"],
        fail_silently=False,
    )
