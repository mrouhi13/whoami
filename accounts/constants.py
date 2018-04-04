from django.utils.translation import ugettext_lazy as _
from djoser.constants import Messages


class CustomMessages(Messages):
    SUCCESS_PROFILE_UPDATE = _('پروفایل شما به‌روز شد.')
    INVALID_CREDENTIALS_ERROR = _('اطلاعات وارد شده صحیح نیست.')
    INACTIVE_ACCOUNT_ERROR = _('این کاربر غیرفعال / حذف شده است.')
    INVALID_TOKEN_ERROR = _('نشان شما مورد تایید نیست.')
    INVALID_TOKEN_HEADER_ERROR_1 = _('خطای سربرگ: نشان شما باطل شده است.')
    INVALID_TOKEN_HEADER_ERROR_2 = _('خطای سربرگ: نشان دارای فاصله است.')
    INVALID_TOKEN_HEADER_ERROR_3 = _('خطای سربرگ: نشان دارای علائم غیرمجاز است.')
    EXPIRED_TOKEN_ERROR = _('نشان شما منقضی شده است.')
    INVALID_UID_ERROR = _('شناسه‌ی کاربر مورد تایید نیست.')
    STALE_TOKEN_ERROR = _('این نشان قبلا استفاده شده است.')
    PASSWORD_MISMATCH_ERROR = _('گذرواژه‌ها یکسان نیست.')
    USERNAME_MISMATCH_ERROR = _('{0}‌ها یکسان نیست.')
    INVALID_PASSWORD_ERROR = _('گذرواژه صحیح نیست.')
    EMAIL_NOT_FOUND = _('کاربری با این ایمیل پیدا نشد.')
    EMAIL_UNIQUE_ERROR = _('این ایمیل قبلا ثبت شده است.')
    CANNOT_CREATE_USER_ERROR = _('نمی‌توان حساب جدید ایجاد کرد.')
    USER_WITHOUT_EMAIL_FIELD_ERROR = _('کاربر فیلد ایمیل ندارد.')
    IS_BLANK = _('{0} وارد نشده است.')
    IS_INVALID = _('{0} صحیح نیست.')
    SHORT_PASSWORD_VALIDATION_ERROR = _("گذرواژه کوتاه است، حداقل %(min_length)d حرف لازم است.")
    SHORT_PASSWORD_VALIDATION_HELP = _("گذرواژه حداقل باید %(min_length)d حرف باشد.")
    SIMILAR_PASSWORD_VALIDATION_ERROR = _("گذرواژه محتوی بخشی از %(verbose_name)s است.")
    SIMILAR_PASSWORD_VALIDATION_HELP = _(
        "گذرواژه نمی‌تواند محتوی بخشی از اطلاعات شخصی شما باشد.")
    COMMON_PASSWORD_VALIDATION_ERROR = _("گذرواژه‌ی انتخاب شده بسیار رایج است.")
    COMMON_PASSWORD_VALIDATION_HELP = _("گذرواژه نمی‌تواند از بین گذرواژه‌های رایج انتخاب شود.")
    NUMERIC_PASSWORD_VALIDATION_ERROR = _("گذرواژه‌ی انتخاب شده فاقد حرف است.")
    NUMERIC_PASSWORD_VALIDATION_HELP = _("گذرواژه نمی‌تواند فقط عدد باشد.")
