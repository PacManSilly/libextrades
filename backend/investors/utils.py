from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from rest_framework.reverse import reverse
from django.core.mail import send_mail
from django.conf import settings

# Custom user model
User = get_user_model()


def send_email_verification(email):
    user = User.objects.get(email=email)
    token = RefreshToken.for_user(user).access_token

    domain = Site.objects.get_current().domain
    rel_link = reverse("verify_email",)
    absolute_url = F"http://{domain}/verify-account/email/?token={token}"

    body = render_to_string(
        'email_verification.txt',
        context={
            'url': absolute_url,
            'company': 'LibExTrades',
            'firstname': user.first_name,
            'wave': '\U0001F44B',
            'heart': '\U0001F499'
        }
    )

    send_mail(
        subject="Verify Your LibExTrades account",
        message=body,
        recipient_list=[user.email, ],
        from_email=settings.DEFAULT_FROM_EMAIL
    )


def resend_email_verification(email):

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        pass
    else:
        token = RefreshToken.for_user(user).access_token

        domain = Site.objects.get_current().domain
        rel_link = reverse("verify_email",)
        absolute_url = F"http://{domain}/verify-account/email/?token={token}"

        body = render_to_string(
            'resend_email_verification.txt',
            context={
                'url': absolute_url,
                'company': 'LibExTrades',
                'firstname': user.first_name,
                'wave': '\U0001F44B',
                'heart': '\U0001F499'
            }
        )

        send_mail(
            subject="Verify Your LibExTrades account",
            message=body,
            recipient_list=[user.email, ],
            from_email=settings.DEFAULT_FROM_EMAIL
        )
