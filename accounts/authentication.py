from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication, get_authorization_header

from accounts.constants import CustomMessages as Messages
from accounts.models import AuthToken


class CustomTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Bearer'
    model = AuthToken

    """
    A custom token model may be used, but must have the following properties.

    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            raise exceptions.AuthenticationFailed(Messages.INVALID_TOKEN_HEADER_ERROR_1)
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed(Messages.INVALID_TOKEN_HEADER_ERROR_2)

        try:
            token = auth[1].decode()
        except UnicodeError:
            raise exceptions.AuthenticationFailed(Messages.INVALID_TOKEN_HEADER_ERROR_3)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(Messages.INVALID_TOKEN_ERROR)

        if token.user.is_suspend:
            raise exceptions.AuthenticationFailed(Messages.SUSPEND_ACCOUNT_ERROR)

        if token.expired():
            token.delete()
            raise exceptions.AuthenticationFailed(Messages.EXPIRED_TOKEN_ERROR)

        return token.user, token
