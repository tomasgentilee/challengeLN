from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from employees.automate import send_salary_report

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Todos los lunes a las 08:00 AM
    scheduler.add_job(
        send_salary_report,
        trigger="cron",
        day_of_week="mon",
        hour=8,
        minute=0,
        id="weekly_salary_report",
        replace_existing=True,
    )

    scheduler.start()
