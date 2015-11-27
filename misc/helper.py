from django.core.mail import EmailMultiAlternatives, get_connection
from django.template import loader, Context
from django.conf import settings
from django.utils.html import strip_tags
from smsandemail.models import EmailLog

__author__ = 'dev'


def email_connection():
    try:
        connection = get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD
        )
        return connection
    except Exception, exc:
        return False


def send_wemed_mail(template_name, email_context, subject, recipients,
                    cc_list=None, sender=None, att_file=None,
                    headers=None):
    """
    This function will send a multi-part e-mail with both HTML and
    Text parts.

    template_name must be an email template with .html extension

    email_context should be a plain python dictionary. It is applied against
        both the email messages (templates) & the subject.

    subject should contain subject template name with .txt extension

    recipients can be either a string, eg 'a@b.com' or a list,
    (or a flat ValuesListQuerySet object) eg:
        ['a@b.com', 'c@d.com']. Type conversion is done if needed.

    sender can be an e-mail, 'Name <email>' or None. If unspecified, the
        DEFAULT_FROM_EMAIL will be used.

    att_file and headers args should always be sent as named arguments

    return: 1 if email successfully sent else 0
    """
    try:
        connection = email_connection()

        if not connection:
            return False
        else:
            if not sender:
                sender = 'WeMed Alert <finallystart15@gmail.com>'
            if 'site' not in email_context:
                email_context.update({'site': settings.SITE})
            context = Context(email_context)

            if not template_name == "":
                html_part = loader.get_template(template_name).render(context)
                text_part = strip_tags(html_part)
            else:
                html_part = ""
                text_part = ""

            subject_part = loader.get_template(subject).render(context)
            subject_part = ''.join(subject_part.splitlines())

            if recipients.__class__.__name__ == 'unicode' \
                    or recipients.__class__.__name__ == 'str':
                recipients = [recipients, ]

            final_recipients = []
            for recipient in recipients:
                """
                  TODO: once we deploy prod this is so that emails are not sent
                  at emails like 1234567890@wemed.com
                 """
                # if not bool(re.match(r'[0-9]{10}@wemed.com$', recipient)):

                final_recipients.append(recipient)
            """
                  TODO: once we deploy prod this is so that emails can be sent
                  to local developers for testing purpose
            """
            # if not os.environ.get('DJANGO_SETTINGS_MODULE', None)
            #  == "wemed.settings.prod":
            # final_recipients = settings.LOCAL_EMAIL_RECIPIENTS
            if cc_list is None:
                cc_list = []
            if headers:
                msg = EmailMultiAlternatives(subject_part, text_part, sender,
                                             final_recipients, cc=cc_list,
                                             headers=headers)
            else:
                msg = EmailMultiAlternatives(subject_part, text_part, sender,
                                             final_recipients, cc=cc_list)
            msg.attach_alternative(html_part, "text/html")

            if att_file:
                msg.attach_file(att_file)

            status = msg.send(fail_silently=True)
            if status == 1:
                status_value = "Sent"
            else:
                status_value = "Failed"
            EmailLog.objects.create(receiver=", ".join(final_recipients),
                                    subject=subject_part, email=html_part,
                                    status=status_value)
            return status

    except Exception, e:
        print e
        return 0