from email.policy import default
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.conf import settings
from django.db import models
import uuid


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

PLANS = (
    ('Starter plan', 'Starter plan'),
    ('Advance plan', 'Advance plan'),
    ('Premium plan', 'Premium plan'),
    ('Sublime plan', 'Sublime plan'),
    ('Luxury plan', 'Luxury plan')
)

METHODS = (
    ('Bitcoin', 'Bitcoin'),
    ('Ethereum', 'Ethereum'),
    ('PayPal', 'PayPal'),
    ('Bank', 'Bank'),
)

STATUS = (
    ('Active', 'Active'),
    ('Pending', 'Pending')
)

WITHDRAWAL_STATUS = (
    ('Pending', 'Pending'),
    ('Declined', 'Declined'),
    ('Processed', 'Processed'),
)


TRANSACTION_TYPE = (
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal'),
)
    

def save_image_investors(instance, filename):
    """
    Function to return the file path to save the mugshot of
    an investor.
    """
    return F"mediafiles/investors/{instance.id}/images/{filename}"


def save_image_experts(instance, filename):
    """
    Function to return the file path to save the mugshot of
    an investor.
    """
    return F"mediafiles/experttraders/{instance.id}/images/{filename}"


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str = None, is_active: bool = True, is_staff: bool = False, is_superuser: bool = False):
        if not email:
            raise ValueError(_("Users must provide an email address"))

        user = self.model(email=self.normalize_email(email.lower()))
        user.is_active = is_active
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser( self, email: str, password: str = None, is_active: bool = True, is_staff: bool = True, is_superuser: bool = True):
        user = self.create_user(
            email=email,
            password=password,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """
    Custom User model
    """
    # Identification
    id = models.CharField(_("ID"), default=uuid.uuid4, max_length=255, unique=True, primary_key=True, editable=False)
    username = models.CharField(_("Username"), max_length=50, blank=True, null=True)
    email = models.EmailField(
        _("Email Address"), unique=True, max_length=255, blank=False,
        error_messages={"unique": _("Investor with this email address already exists")}
    )
    phone = models.CharField(_("Phone Number"), max_length=50, blank=True, null=True, help_text=_("Investor phone number"))
    password = models.CharField(
        _("Password"), max_length=128, help_text=_("Investor password"),
        validators=[
            validators.MinLengthValidator(limit_value=8),
            validators.RegexValidator(
                regex=r'\s',
                message=_("Password cannot contain spaces"),
                inverse_match=True
            )
        ]
    )
    is_verified = models.BooleanField(
        _("Is Verified"), default=False, blank=False, null=False,
        help_text=_("Investor email address is verified")
    )

    is_suspended = models.BooleanField(default=False, blank=True, null=False, help_text=_("Is this user suspended or not"))

    kyc_front_view = models.ImageField(_("KYC Front View"), upload_to=save_image_investors, blank=True, null=True, help_text=_("KYC front view"))
    kyc_back_view = models.ImageField(_("KYC Back View"), upload_to=save_image_investors, blank=True, null=True, help_text=_("KYC back view"))

    # bio
    first_name = models.CharField(_("First Name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True, null=True)
    other_name = models.CharField(_("Other Name"), max_length=255, blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=7, choices=GENDER, blank=True, null=True)
    mugshot = models.ImageField(_("Mugshot"), upload_to=save_image_investors, blank=True)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False, blank=True, null=True)

    # Address
    country = models.CharField(_("Country"), max_length=255, blank=True, null=True)
    state = models.CharField(_("State"), max_length=255, blank=True, null=True)
    city = models.CharField(_("City"), max_length=255, blank=True, null=True)
    postal = models.CharField(_("Postal/ZIP"), max_length=20, blank=True, null=True)

    # investment
    investment_plan = models.CharField(_("Investment Plan"), max_length=255, blank=True, null=False, default="....", help_text=_("Investors investment plan"))
    account_balance = models.CharField(_("Account balance"), max_length=50, blank=True, null=False, default="0.00", help_text=_("Investors acount balance"))
    total_profit = models.CharField(_("Total profit"), max_length=50, blank=True, null=False, default="0.00", help_text=_("Investors total profit"))
    total_trade = models.IntegerField(_("Total trades"), blank=True, null=False, default="0", help_text=_("Investors total trades"))
    referral_bonus = models.CharField(_("Referral bonus"), max_length=50, blank=True, null=False, default="0.00", help_text=_("Investors referral bonus"))
    total_deposit = models.CharField(_("Total deposit"), max_length=50, blank=True, null=False, default="0.00", help_text=_("Investors total deposit"))
    total_withdrawal = models.CharField(_("Total withdrawal"), max_length=50, blank=True, null=False, default="0.00", help_text=_("Investors total withdrawal"))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    def get_full_name(self) -> str:
        return F"{self.first_name or ''} {self.last_name or ''} {self.other_name or ''}"


class Transaction(models.Model):
    """
    Investors transactions
    """
    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False, help_text=_("Database ID"))
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Investor"), on_delete=models.CASCADE)
    transaction_type = models.CharField(_("Status"), choices=TRANSACTION_TYPE, max_length=10, default='Pending', help_text=_("Transaction type"))
    amount = models.CharField(_("Amount"), max_length=50, blank=True, null=True, help_text=_("Amount invested in this plan"))
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    status = models.CharField(_("Status"), choices=STATUS, max_length=10, default='Pending', help_text=_("Status of this investment"))

    def __str__(self) -> str:
        return f"{self.investor} - {self.transaction_type}"


class InvestorInvestment(models.Model):
    """
    Investors investments model
    """
    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False, help_text=_("Database ID"))
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Investor"), on_delete=models.CASCADE)
    plan = models.CharField(_("Plan"), max_length=255, choices=PLANS, default='Starter plan', blank=False, null=False)
    amount = models.CharField(_("Amount"), max_length=50, blank=True, null=True, help_text=_("Amount invested in this plan"))
    days = models.CharField(_("Days"), max_length=50, blank=True, null=True, default='')
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    status = models.CharField(_("Status"), choices=STATUS, max_length=10, default='Pending', help_text=_("Status of this investment"))
    
    # class Meta:
    #     verbose_name_plural = ''

    def __str__(self):
        return F"{self.investor} - ({self.plan}) - (${self.amount})"


class InvestorWithdrawal(models.Model):
    """
    Investors withdrawal model
    """
    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False, help_text=_("Database ID"))
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Investor"), on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    method = models.CharField(_("Method"), max_length=50, choices=METHODS, blank=False, null=False, default='Bitcoin')
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True, help_text=_("Wallet address"))
    email = models.CharField(_("Email"), max_length=255, blank=True, null=True, help_text=_("PayPal email address"))
    bank_name = models.CharField(_("Bank Name"), max_length=255, blank=True, null=True, help_text=_("Name of recieving bank"))
    account_number = models.CharField(_("Account Number"), max_length=255, blank=True, null=True, help_text=_("Bank account number"))
    swift_code = models.CharField(_("Swift Code"), max_length=255, blank=True, null=True, help_text=_("Bank Swift Code"))
    amount = models.CharField(_("Amount"), max_length=50, blank=True, null=True, help_text=_("Amount to withdraw"))
    status = models.CharField(_("Status"), choices=WITHDRAWAL_STATUS, max_length=10, default='Pending', help_text=_("Status of this withdrawal"))

    def __str__(self):
        return F"{self.investor} - ({self.method}) - (${self.amount})"


class ExpertTraders(models.Model):
    id = models.CharField(_("ID"), default=uuid.uuid4, max_length=255, unique=True, primary_key=True, editable=False)
    email = models.EmailField(_("Email Address"), max_length=254, blank=True, null=True)
    investors = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Investors"), blank=True, help_text=_("Investors linked with this trader"))
    mugshot = models.ImageField(_("Mugshot"), upload_to=save_image_experts, blank=True, null=True)
    full_name = models.CharField(_("Full Name"), max_length=255, blank=False, null=False, help_text=_("Trader full name"))
    win_rate = models.CharField(_("Win Rate"), max_length=50, blank=True, null=True, default="90%")
    profit_share = models.CharField(_("Profit Share"), max_length=50, blank=True, null=True, default="20%")

    class Meta:
        verbose_name_plural = 'ExpertTraders'

    def __str__(self):
        return self.full_name
