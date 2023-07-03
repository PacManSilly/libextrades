from .models import User, InvestorInvestment, InvestorWithdrawal, ExpertTraders, Transaction
from .forms import CustomAppUserCreationForm, CustomAppUserChangeForm
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.contrib import admin


class MyAdmin(admin.AdminSite):
    site_header = "LibExTrades Administration"


class UserModelAdmin(UserAdmin):
    add_form = CustomAppUserCreationForm
    form = CustomAppUserChangeForm

    list_display = ('id', 'email', 'phone', 'first_name', 'last_name', 'is_verified')
    list_display_links = ('id', 'email', )
    list_filter = ('is_verified', )

    add_fieldsets = (
        ("Identification", {"fields": ("email", )}),
        ("Security", {"fields": ("password1", "password2")}),
    )

    fieldsets = (
        ("Identification", {"fields": ("id", "email", "phone", "password", "kyc_front_view", "kyc_back_view"), }),
        ("Bio", {"fields": ("first_name", "last_name", "other_name", "dob", "gender", "mugshot"), }),
        ("Location", {"fields": ("country", "state", "city", "postal", )}),
        ("Investment", {"fields": ("account_balance", "total_profit", "bonus", "referral_bonus", "total_deposit", "total_withdrawal")}),
        ("Status", {"fields": ("is_verified", "is_suspended", "is_active", "is_staff", "is_superuser"), }),
        ("Groups & Permissions", {"fields": ("groups", "user_permissions"), }),
        ("Important Dates", {"fields": ("date_joined", "last_login"), }),
    )

    readonly_fields = ('id', 'password', 'date_joined', 'last_login')
    ordering = ('-date_joined',)
    radio_fields = {"gender": admin.HORIZONTAL}


class InvestorInvestmentAdmin(admin.ModelAdmin):
    model = InvestorInvestment
    list_display = ('id', 'investor', 'plan', 'amount', 'created', 'status')
    list_display_links = ('id', 'investor')
    list_filter = ('plan', 'investor', 'created')


class InvestorWithdrawalAdmin(admin.ModelAdmin):
    model = InvestorWithdrawal
    list_display = ('id', 'investor', 'method', 'created')
    list_display_links = ('id', 'investor')
    list_filter = ('method',)


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('id', 'investor', 'transaction_type', 'created')
    list_display_links = ('id', 'investor')
    list_filter = ('transaction_type', 'status')
    

class ExpertTradersAdmin(admin.ModelAdmin):
    model = ExpertTraders
    list_display = ('id', 'full_name', 'win_rate', 'profit_share')
    list_display_links = ('id', 'full_name')



admin_site = MyAdmin(name='admin')
admin_site.register(Site)
admin_site.register(Group)
admin_site.register(Token)
admin_site.register(User, UserModelAdmin)
admin_site.register(InvestorInvestment, InvestorInvestmentAdmin)
admin_site.register(InvestorWithdrawal, InvestorWithdrawalAdmin)
admin_site.register(ExpertTraders, ExpertTradersAdmin)
admin_site.register(Transaction, TransactionAdmin)
