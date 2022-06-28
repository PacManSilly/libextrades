from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.conf import settings
from django.db import models


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

PLANS = (
    ('Starter plan', 'Starter plan'),
    ('Advance plan', 'Advance plan'),
    ('Starter basic advance plan', 'Starter basic advance plan'),
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


def save_image(instance, filename):
    """
    Function to return the file path to save the mugshot of
    an investor.
    """
    return F"investors/{instance.id}/images/{filename}"


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
    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False, help_text=_("Database ID"))
    username = models.CharField(_("Username"), max_length=50, blank=True, null=True)
    email = models.EmailField(
        _("Email Address"), unique=True, max_length=255, blank=False,
        error_messages={"unique": _("Investor email address")}
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
    kyc_front_view = models.ImageField(_("KYC Front View"), upload_to=save_image, blank=True, null=True, help_text=_("KYC front view"))
    kyc_back_view = models.ImageField(_("KYC Back View"), upload_to=save_image, blank=True, null=True, help_text=_("KYC back view"))

    # bio
    first_name = models.CharField(_("First Name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=255, blank=True, null=True)
    other_name = models.CharField(_("Other Name"), max_length=255, blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=7, choices=GENDER, blank=True, null=True)
    mugshot = models.ImageField(_("Mugshot"), upload_to=save_image, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False, blank=True, null=True)

    # Address
    country = models.CharField(_("Country"), max_length=255, blank=True, null=True)
    state = models.CharField(_("State"), max_length=255, blank=True, null=True)
    city = models.CharField(_("City"), max_length=255, blank=True, null=True)
    postal = models.CharField(_("Postal/ZIP"), max_length=20, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

    def get_full_name(self) -> str:
        return F"{self.first_name or ''} {self.last_name or ''} {self.other_name or ''}"


class InvestorInvestment(models.Model):
    """
    Investors investments model
    """
    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False, help_text=_("Database ID"))
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Investor"), on_delete=models.CASCADE)
    plan = models.CharField(_("Plan"), max_length=255, choices=PLANS, default='Starter plan', blank=False, null=False)
    amount = models.CharField(_("Amount"), max_length=50, blank=True, null=True, help_text=_("Amount invested in this plan"))
    created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    status = models.CharField(_("Status"), choices=STATUS, max_length=10, default='Pending', help_text=_("Status of this investment"))
    
    # class Meta:
    #     verbose_name_plural = ''

    def __str__(self):
        return F"{self.investor} - ({self.plan})"


class InvestorWithdrawal(models.Model):
    """
    Investors withdrawal model
    """
    id = models.BigAutoField(_("ID"), unique=True, primary_key=True, editable=False, help_text=_("Database ID"))
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Investor"), on_delete=models.CASCADE)
    created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)
    method = models.CharField(_("Method"), max_length=50, choices=METHODS, blank=False, null=False, default='Bitcoin')
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True, help_text=_("Wallet address"))
    email = models.CharField(_("Email"), max_length=255, blank=True, null=True, help_text=_("PayPal email address"))
    bank_name = models.CharField(_("Bank Name"), max_length=255, blank=True, null=True, help_text=_("Name of recieving bank"))
    account_number = models.CharField(_("Account Number"), max_length=255, blank=True, null=True, help_text=_("Bank account number"))
    swift_code = models.CharField(_("Swift Code"), max_length=255, blank=True, null=True, help_text=_("Bank Swift Code"))
    amount = models.CharField(_("Amount"), max_length=50, blank=True, null=True, help_text=_("Amount to withdraw"))

    def __str__(self):
        return F"{self.investor} - ({self.method}) - ({self.amount})"
