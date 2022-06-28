from .forms import CustomAppUserCreationForm, CustomAppUserChangeForm
from .models import User, InvestorInvestment, InvestorWithdrawal
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

    list_display = ('id', 'first_name', 'last_name', 'email', 'is_verified')
    list_display_links = ('email', )
    list_filter = ('is_verified', )

    add_fieldsets = (
        ("Identification", {"fields": ("email", )}),
        ("Security", {"fields": ("password1", "password2")}),
    )

    fieldsets = (
        ("Identification", {"fields": ("id", "email", "password", "kyc_front_view", "kyc_back_view"), }),
        ("Bio", {"fields": ("first_name", "last_name", "other_name", "dob", "gender", "mugshot"), }),
        ("Location", {"fields": ("country", "state", "city", "postal", )}),
        ("Status", {"fields": ("is_verified", "is_active", "is_staff", "is_superuser"), }),
        ("Groups & Permissions", {"fields": ("groups", "user_permissions"), }),
        ("Important Dates", {"fields": ("date_joined", "last_login"), }),
    )

    readonly_fields = ('id', 'password', 'date_joined', 'last_login')
    ordering = ('-date_joined',)
    radio_fields = {"gender": admin.HORIZONTAL}


class InvestorInvestmentAdmin(admin.ModelAdmin):
    model = InvestorInvestment


class InvestorWithdrawalAdmin(admin.ModelAdmin):
    model = InvestorWithdrawal
    list_filter = ('method', )


admin_site = MyAdmin(name='admin')
admin_site.register(Site)
admin_site.register(Group)
admin_site.register(Token)
admin_site.register(User, UserModelAdmin)
admin_site.register(InvestorInvestment, InvestorInvestmentAdmin)
admin_site.register(InvestorWithdrawal, InvestorWithdrawalAdmin)
