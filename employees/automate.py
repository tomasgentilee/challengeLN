from django.db.models import Avg, Min, Max
from django.core.mail import send_mail
from .models import Employee

def send_salary_report():
    stats = Employee.objects.aggregate(
        avg=Avg("salary"),
        min=Min("salary"),
        max=Max("salary"),
    )

    avg_salary = stats["avg"] or 0
    min_salary = stats["min"] or 0
    max_salary = stats["max"] or 0

    subject = "Weekly Salary Report"
    message = (
        f"Salary Report (Weekly)\n\n"
        f"Average Salary: {avg_salary:.2f} USD\n"
        f"Minimum Salary: {min_salary:.2f} USD\n"
        f"Maximum Salary: {max_salary:.2f} USD\n"
    )

    send_mail(
        subject=subject,
        message=message,
        from_email="noreply@peopleflow.com",
        recipient_list=["nacho@peopleflow.com"],
        fail_silently=False,
    )
