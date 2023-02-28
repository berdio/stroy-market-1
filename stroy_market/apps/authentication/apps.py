from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authentication'
    verbose_name = _("Users")

    def ready(self):
        try:
            import stroymarket.users.signals  # noqa F401
        except ImportError:
            pass