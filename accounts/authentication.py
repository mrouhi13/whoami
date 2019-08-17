from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:

        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Bearer'

    """
    A custom token model may be used, but must have the following properties.

    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if token.user.is_suspend:
            raise exceptions.AuthenticationFailed(
                _('This account has suspended.'))

        return token.user, token
