from cmath import e
from rest_framework.authtoken.models import Token
from .utils import send_email_verification


def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        send_email_verification(email=instance.email)
