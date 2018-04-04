import re
from difflib import SequenceMatcher

from django.contrib.auth.password_validation import (
    MinimumLengthValidator,
    UserAttributeSimilarityValidator,
    CommonPasswordValidator,
    NumericPasswordValidator
)
from django.core.exceptions import (
    FieldDoesNotExist, )
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _, ngettext

from accounts.constants import CustomMessages as Messages


class CustomMinimumLengthValidator(MinimumLengthValidator):
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    Messages.SHORT_PASSWORD_VALIDATION_ERROR,
                    Messages.SHORT_PASSWORD_VALIDATION_ERROR,
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            Messages.SHORT_PASSWORD_VALIDATION_HELP,
            Messages.SHORT_PASSWORD_VALIDATION_HELP,
            self.min_length
        ) % {'min_length': self.min_length}


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_parts = re.split(r'\W+', value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        Messages.SIMILAR_PASSWORD_VALIDATION_ERROR,
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )

    def get_help_text(self):
        return Messages.SIMILAR_PASSWORD_VALIDATION_HELP


class CustomCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                Messages.COMMON_PASSWORD_VALIDATION_ERROR,
                code='password_too_common',
            )

    def get_help_text(self):
        return Messages.COMMON_PASSWORD_VALIDATION_HELP


class CustomNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                Messages.NUMERIC_PASSWORD_VALIDATION_ERROR,
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return Messages.NUMERIC_PASSWORD_VALIDATION_HELP
