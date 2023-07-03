from .utils import send_email_verification
from .models import Transaction


def new_user(sender, instance=None, created=False, **kwargs):
    if created:
        send_email_verification(email=instance.email)


def new_deposit(sender, instance=None, created=False, **kwargs):
    if created:
        Transaction.objects.create(
            investor=instance.investor,
            transaction_type="Deposit",
            amount=instance.amount
        )


def new_withdrawal(sender, instance=None, created=False, **kwargs):
    if created:
        Transaction.objects.create(
            investor=instance.investor,
            transaction_type="Withdrawal",
            amount=instance.amount
        )