from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from profile.models import AuthToken


class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    model = AuthToken

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('نشان شما مورد تایید نیست'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(
                _('این کاربر غیرفعال / حذف شده است.'))

        if token.expired():
            token.delete()
            raise exceptions.AuthenticationFailed('نشان شما منقضی شده است.')

        return (token.user, token)
