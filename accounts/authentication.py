from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from accounts.constants import CustomMessages as Messages
from accounts.models import AuthToken


class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    model = AuthToken

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(Messages.INVALID_TOKEN_ERROR)

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(Messages.INACTIVE_ACCOUNT_ERROR)

        if token.expired():
            token.delete()
            raise exceptions.AuthenticationFailed(Messages.EXPIRED_TOKEN_ERROR)

        return token.user, token
