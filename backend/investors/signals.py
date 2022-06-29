from .utils import send_email_verification


def new_user(sender, instance=None, created=False, **kwargs):
    if created:
        send_email_verification(email=instance.email)
