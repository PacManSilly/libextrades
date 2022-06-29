from django.db.models.signals import post_save
from django.apps import AppConfig
from django.conf import settings
import uuid


class InvestorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'investors'
    def ready(self) -> None:
        from . import signals

        post_save.connect(signals.new_user, sender=settings.AUTH_USER_MODEL, dispatch_uid=uuid.uuid4())