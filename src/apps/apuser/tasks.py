from datetime import timedelta
from celery.task import periodic_task
from template_email import TemplateEmail
from apuser.models.profile import EmailDelivery


@periodic_task(run_every=timedelta(minutes=1))
def send_email():
    qs = EmailDelivery.objects.filter(status=EmailDelivery.NEW)
    for e in qs:
        email = TemplateEmail(
            to=e.email.split(','),
            template='email/%s' % e.template,
            context=e.context
        )
        email.send()
        e.status = EmailDelivery.SUBMITTED
        e.save()


# @periodic_task(run_every=timedelta(days=1))
# def check_user_age():
#     # e = EmailDelivery(
#     #     template='operator/x_notification.html'
#     # )
#     pass