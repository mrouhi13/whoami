from django.contrib.auth.tokens import default_token_generator
from djoser import utils, email, conf as djoser_conf

import ponera


class ActivationEmail(email.ActivationEmail):
    def get_context_data(self):
        context = super(ActivationEmail, self).get_context_data()

        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = djoser_conf.settings.ACTIVATION_URL.format(**context)
        context['protocol'] = ponera.settings.EMAIL_URL_SCHEMA
        context['domain'] = 'activation'
        return context


class PasswordResetEmail(email.PasswordResetEmail):
    def get_context_data(self):
        context = super(PasswordResetEmail, self).get_context_data()

        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = djoser_conf.settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        context['protocol'] = ponera.settings.EMAIL_URL_SCHEMA
        context['domain'] = 'password-reset'
        return context
