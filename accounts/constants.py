from django.utils.translation import ugettext_lazy as _
from djoser.constants import Messages


class CustomMessages(Messages):
    SUSPEND_ACCOUNT_ERROR = _('User account is suspended.')
